from apps.symbol import keylink, metadata, multisig, restrictionaccount
from trezor import wire
from trezor.crypto.curve import ed25519
from trezor.messages.SymbolSignedTx import SymbolSignedTx
from trezor.messages.SymbolSignTx import SymbolSignTx

from apps.common import seed
from apps.common.keychain import with_slip44_keychain
from apps.common.paths import validate_path

from . import CURVE, PATTERN, SLIP44_ID, transfer, mosaic, namespace, lockhash, locksecret
#from .helpers import NEM_HASH_ALG, check_path
#from .validators import validate


@with_slip44_keychain(PATTERN, slip44_id=SLIP44_ID, curve=CURVE)
async def sign_tx(ctx, msg: SymbolSignTx, keychain):

    #TODO: SYMBOL DEBUG
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

    await validate_path(
        ctx,
        keychain,
        msg.transaction.address_n,
    )


    node       = keychain.derive(msg.transaction.address_n)
    public_key = seed.remove_ed25519_prefix(node.public_key())
    common     = msg.transaction



    if msg.transfer:
        tx = await transfer.transfer(ctx, common, msg.transfer)
    elif msg.mosaic_definition:
        tx = await mosaic.definition(ctx, common, msg.mosaic_definition)
    elif msg.mosaic_supply_change:
        tx = await mosaic.supply_change(ctx, common, msg.mosaic_supply_change)
    elif msg.namespace_registration:
        tx = await namespace.register(ctx, common, msg.namespace_registration)
    elif msg.address_alias:
        tx = await namespace.address_alias(ctx, common, msg.address_alias)
    elif msg.mosaic_alias:
        tx = await namespace.mosaic_alias(ctx, common, msg.mosaic_alias)
    elif msg.account_key_link:
        tx = await keylink.account_key_link(ctx, common, msg.account_key_link)
    elif msg.node_key_link:
        tx = await keylink.node_key_link(ctx, common, msg.node_key_link)
    elif msg.vrf_key_link:
        tx = await keylink.vrf_key_link(ctx, common, msg.vrf_key_link)
    elif msg.voting_key_link:
        tx = await keylink.voting_key_link(ctx, common, msg.voting_key_link)
    elif msg.hash_lock:
        tx = await lockhash.hash_lock(ctx, common, msg.hash_lock)
    elif msg.secret_lock:
        tx = await locksecret.secret_lock(ctx, common, msg.secret_lock)
    elif msg.secret_proof:
        tx = await locksecret.secret_proof(ctx, common, msg.secret_proof)
    elif msg.account_metadata:
        tx = await metadata.account_metadata(ctx, common, msg.account_metadata)
    elif msg.mosaic_metadata:
        tx = await metadata.mosaic_metadata(ctx, common, msg.mosaic_metadata)
    elif msg.namespace_metadata:
        tx = await metadata.namespace_metadata(ctx, common, msg.namespace_metadata)
    elif msg.multisig_account_modification:
        tx = await multisig.multisig_account_modification(ctx, common, msg.multisig_account_modification)
    elif msg.account_address_restriction:
        tx = await restrictionaccount.account_address_restriction(ctx, common, msg.account_address_restriction)
    elif msg.account_mosaic_restriction:
        tx = await restrictionaccount.account_mosaic_restriction(ctx, common, msg.account_mosaic_restriction)
    elif msg.account_operation_restriction:
        tx = await restrictionaccount.account_operation_restriction(ctx, common, msg.account_operation_restriction)
    else:
        raise wire.DataError("No transaction provided")

    signature = ed25519.sign(node.private_key(), tx, "keccak") #change to sha3-256

    return SymbolSignedTx(
        data=tx,
        signature=signature,
    )
