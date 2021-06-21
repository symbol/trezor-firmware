# This file is part of the Trezor project.
#
# Copyright (C) 2012-2019 SatoshiLabs and contributors
#
# This library is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License version 3
# as published by the Free Software Foundation.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the License along with this library.
# If not, see <https://www.gnu.org/licenses/lgpl-3.0.html>.

from trezorlib.messages import SymbolEntityType
from . import exceptions, messages
from .tools import expect

def create_transaction_header(transaction):
    msg = messages.SymbolHeader()
    msg.signer_public_key = transaction["signer_public_key"]
    msg.version           = transaction["version"]
    msg.network_type      = transaction["network_type"]

    if "max_fee" in transaction:
        msg.max_fee       = transaction["max_fee"]
        msg.deadline      = transaction["deadline"]

    return msg


def create_transfer(transaction):
    msg = messages.SymbolTransfer()

    msg.recipient_address = transaction["recipient_address"]

    if "mosaics" in transaction:
        msg.mosaics = [
            messages.SymbolMosaic(
                id=mosaic["id"],
                amount=mosaic["amount"]
            )
            for mosaic in transaction["mosaics"]
        ]

    if "message" in transaction:
        msg.message = bytes.fromhex(transaction["message"])

    return msg


def create_mosaic_supply_change(transaction):
    msg = messages.SymbolMosaicSupplyChange()

    mosaic = transaction["mosaic"]
    msg.mosaic = messages.SymbolMosaic(id=mosaic["id"], amount=mosaic["amount"])
    msg.action = transaction["action"]

    return msg


def create_mosaic_definition(transaction):
    msg = messages.SymbolMosaicDefinition()

    msg.id = transaction["id"]
    msg.duration = transaction["duration"]
    msg.nonce = transaction["nonce"]
    msg.flags = transaction["flags"]
    msg.divisibility = transaction["divisibility"]

    return msg

def create_namespace_registration(transaction):
    msg = messages.SymbolNamespaceRegistration()

    msg.duration          = transaction["duration"]
    msg.parent_id         = transaction["parent_id"]
    msg.id                = transaction["id"]
    msg.registration_type = transaction["registration_type"]
    msg.name              = transaction["name"]

    return msg

def create_address_alias(transaction):
    msg = messages.SymbolAddressAlias()

    msg.namespace_id = transaction["namespace_id"]
    msg.address      = transaction["address"]
    msg.action       = transaction["action"]

    return msg

def create_mosaic_alias(transaction):
    msg = messages.SymbolMosaicAlias()

    msg.namespace_id = transaction["namespace_id"]
    msg.mosaic_id    = transaction["mosaic_id"]
    msg.action       = transaction["action"]

    return msg

def create_key_link(transaction):
    msg = messages.SymbolKeyLink()

    msg.public_key = transaction["public_key"]
    msg.action     = transaction["action"]

    return msg

def create_voting_key_link(transaction):
    msg = messages.SymbolVotingKeyLink()

    msg.public_key  = transaction["public_key"]
    msg.start_point = transaction["start_point"]
    msg.end_point   = transaction["end_point"]
    msg.action      = transaction["action"]

    return msg

def create_hash_lock(transaction):
    msg = messages.SymbolHashLock()

    mosaic = transaction["mosaic"]
    msg.mosaic   = messages.SymbolMosaic(id=mosaic["id"], amount=mosaic["amount"])
    msg.duration = transaction["duration"]
    msg.hash     = transaction["hash"]

    return msg

def create_secret_lock(transaction):
    msg = messages.SymbolSecretLock()

    msg.recipient      = transaction["recipient"]
    msg.secret         = transaction["secret"]
    mosaic             = transaction["mosaic"]
    msg.mosaic         = messages.SymbolMosaic(id=mosaic["id"], amount=mosaic["amount"])
    msg.duration       = transaction["duration"]
    msg.hash_algorithm = transaction["hash_algorithm"]

    return msg

def create_secret_proof(transaction):
    msg = messages.SymbolSecretProof()

    msg.recipient      = transaction["recipient"]
    msg.secret         = transaction["secret"]
    msg.hash_algorithm = transaction["hash_algorithm"]
    msg.proof          = transaction["proof"]

    return msg



def create_common_metadata(transaction, msg):
    msg.address             = transaction["address"]
    msg.scoped_metadata_key = transaction["scoped_metadata_key"]
    msg.value_size_delta    = transaction["value_size_delta"]
    msg.value               = bytes.fromhex(transaction["value"])

def create_account_metadata(transaction):
    msg = messages.SymbolAccountMetadata()
    create_common_metadata(transaction, msg)
    return msg

def create_mosaic_metadata(transaction):
    msg = messages.SymbolMosaicNamespaceMetadata()
    msg.header = messages.SymbolAccountMetadata()

    msg.target_id = transaction["target_id"]
    create_common_metadata(transaction, msg.header)    

    return msg

def create_multisig_account_modification(transaction):
    msg = messages.SymbolMultisigAccountModification()

    msg.min_removal_delta  = transaction["min_removal_delta"]
    msg.min_approval_delta = transaction["min_approval_delta"]
    msg.address_additions  = transaction["address_additions"]
    msg.address_deletions  = transaction["address_deletions"]

    return msg

def create_account_address_restriction(transaction):
    msg = messages.SymbolAccountAddressRestriction()

    msg.type = transaction["restriction_type"]
    msg.additions = transaction["additions"]
    msg.deletions = transaction["deletions"]

    return msg

def create_account_mosaic_restriction(transaction):
    msg = messages.SymbolAccountMosaicRestriction()

    msg.type = transaction["restriction_type"]
    msg.additions = transaction["additions"]
    msg.deletions = transaction["deletions"]

    return msg

def create_account_operation_restriction(transaction):
    msg = messages.SymbolAccountOperationRestriction()

    msg.type = transaction["restriction_type"]
    msg.additions = transaction["additions"]
    msg.deletions = transaction["deletions"]

    return msg

def create_mosaic_address_restriction(transaction):
    msg = messages.SymbolMosaicAddressRestriction()

    msg.mosaic_id = transaction["mosaic_id"]
    msg.restriction_key = transaction["restriction_key"]
    msg.previous_restriction_value = transaction["previous_restriction_value"]
    msg.new_restriction_value = transaction["new_restriction_value"]
    msg.target_address = transaction["target_address"]

    return msg

def create_mosaic_global_restriction(transaction):
    msg = messages.SymbolMosaicGlobalRestriction()

    msg.mosaic_id = transaction["mosaic_id"]
    msg.reference_mosaic_id = transaction["reference_mosaic_id"]
    msg.restriction_key = transaction["restriction_key"]
    msg.previous_restriction_value = transaction["previous_restriction_value"]
    msg.new_restriction_value = transaction["new_restriction_value"]
    msg.previous_restriction_type = transaction["previous_restriction_type"]
    msg.new_restriction_type = transaction["new_restriction_type"]

    return msg

def create_aggregate_transaction(transaction):
    msg = messages.SymbolAggregateTransaction()

    msg.transactions_hash = transaction["transactions_hash"]

    for etxn in transaction["embedded_transactions"]:
        single        = create_single_transaction(etxn)
        single.header = create_transaction_header(etxn)

        msg.transactions.append( single )

#        single = messages.SymbolSingleTransaction()
#        fill_transaction_by_type(single, etxn)
#        msg.transactions.append( single )

    return msg

def fill_transaction_by_type(msg: messages.SymbolSingleTransaction, transaction):
    if transaction["type"] == SymbolEntityType.TRANSFER:
        msg.transfer = create_transfer(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_SUPPLY_CHANGE:
        msg.mosaic_supply_change = create_mosaic_supply_change(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_DEFINITION:
        msg.mosaic_definition = create_mosaic_definition(transaction)
    elif transaction["type"] == SymbolEntityType.NAMESPACE_REGISTRATION:
        msg.namespace_registration = create_namespace_registration(transaction)
    elif transaction["type"] == SymbolEntityType.ADDRESS_ALIAS:
        msg.address_alias = create_address_alias(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_ALIAS:
        msg.mosaic_alias = create_mosaic_alias(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_KEY_LINK:
        msg.account_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.NODE_KEY_LINK:
        msg.node_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.VRF_KEY_LINK:
        msg.vrf_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.VOTING_KEY_LINK:
        msg.voting_key_link = create_voting_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.HASH_LOCK:
        msg.hash_lock = create_hash_lock(transaction)
    elif transaction["type"] == SymbolEntityType.SECRET_LOCK:
        msg.secret_lock = create_secret_lock(transaction)
    elif transaction["type"] == SymbolEntityType.SECRET_PROOF:
        msg.secret_proof = create_secret_proof(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_METADATA:
        msg.account_metadata = create_account_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_METADATA:
        msg.mosaic_metadata = create_mosaic_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.NAMESPACE_METADATA:
        msg.namespace_metadata = create_mosaic_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.MULTISIG_ACCOUNT_MODIFICATION:
        msg.multisig_account_modification = create_multisig_account_modification(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_ADDRESS_RESTRICTION:
        msg.account_address_restriction = create_account_address_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_MOSAIC_RESTRICTION:
        msg.account_mosaic_restriction = create_account_mosaic_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_OPERATION_RESTRICTION:
        msg.account_operation_restriction = create_account_operation_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_ADDRESS_RESTRICTION:
        msg.mosaic_address_restriction = create_mosaic_address_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_GLOBAL_RESTRICTION:
        msg.mosaic_global_restriction = create_mosaic_global_restriction(transaction)
    else:
        print("transaction type: %s" % transaction["type"])
        raise ValueError("Unknown transaction type")

def create_single_transaction( transaction ):
    msg = messages.SymbolSingleTransaction()

    if transaction["type"] == SymbolEntityType.TRANSFER:
        msg.transfer = create_transfer(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_SUPPLY_CHANGE:
        msg.mosaic_supply_change = create_mosaic_supply_change(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_DEFINITION:
        msg.mosaic_definition = create_mosaic_definition(transaction)
    elif transaction["type"] == SymbolEntityType.NAMESPACE_REGISTRATION:
        msg.namespace_registration = create_namespace_registration(transaction)
    elif transaction["type"] == SymbolEntityType.ADDRESS_ALIAS:
        msg.address_alias = create_address_alias(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_ALIAS:
        msg.mosaic_alias = create_mosaic_alias(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_KEY_LINK:
        msg.account_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.NODE_KEY_LINK:
        msg.node_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.VRF_KEY_LINK:
        msg.vrf_key_link = create_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.VOTING_KEY_LINK:
        msg.voting_key_link = create_voting_key_link(transaction)
    elif transaction["type"] == SymbolEntityType.HASH_LOCK:
        msg.hash_lock = create_hash_lock(transaction)
    elif transaction["type"] == SymbolEntityType.SECRET_LOCK:
        msg.secret_lock = create_secret_lock(transaction)
    elif transaction["type"] == SymbolEntityType.SECRET_PROOF:
        msg.secret_proof = create_secret_proof(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_METADATA:
        msg.account_metadata = create_account_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_METADATA:
        msg.mosaic_metadata = create_mosaic_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.NAMESPACE_METADATA:
        msg.namespace_metadata = create_mosaic_metadata(transaction)
    elif transaction["type"] == SymbolEntityType.MULTISIG_ACCOUNT_MODIFICATION:
        msg.multisig_account_modification = create_multisig_account_modification(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_ADDRESS_RESTRICTION:
        msg.account_address_restriction = create_account_address_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_MOSAIC_RESTRICTION:
        msg.account_mosaic_restriction = create_account_mosaic_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.ACCOUNT_OPERATION_RESTRICTION:
        msg.account_operation_restriction = create_account_operation_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_ADDRESS_RESTRICTION:
        msg.mosaic_address_restriction = create_mosaic_address_restriction(transaction)
    elif transaction["type"] == SymbolEntityType.MOSAIC_GLOBAL_RESTRICTION:
        msg.mosaic_global_restriction = create_mosaic_global_restriction(transaction)
    else:
        print("transaction type: %s" % transaction["type"])
        raise ValueError("Unknown transaction type")

    return msg

def create_sign_tx(transaction):
    msg = messages.SymbolSignTx()
    header = create_transaction_header(transaction)

    if transaction["type"] == SymbolEntityType.AGGREGATE_TRANSACTION_COMPLETE:
        msg.aggregate = create_aggregate_transaction(transaction)
        msg.aggregate.header = header
    else:
        msg.single = create_single_transaction(transaction)
        msg.single.header = header

    return msg







# ====== Client functions ====== #

@expect(messages.SymbolSignedTx)
def sign_tx(client, n, transaction):
    try:
        msg = create_sign_tx(transaction)
    except ValueError as e:
        raise exceptions.TrezorException("Failed to encode transaction") from e

    #assert msg.transaction is not None
    assert msg.aggregate or msg.single

    msg.address_n = n

    print("\n\n\n\n\n!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(msg)
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n\n\n\n\n")

    return client.call(msg)
