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

from trezorlib.messages.SymbolMosaicDefinition import SymbolMosaicDefinition
from trezorlib.messages.SymbolNamespaceRegistration import SymbolNamespaceRegistration
from trezorlib.messages import SymbolEntityType
from . import exceptions, messages
from .tools import expect

def create_transaction_common(transaction):
    msg = messages.SymbolTransactionCommon()
    msg.signer_public_key = transaction["signer_public_key"]
    msg.version           = transaction["version"]
    msg.network_type      = transaction["network_type"]
    msg.max_fee           = transaction["max_fee"]
    msg.deadline          = transaction["deadline"]

    return msg


def create_transfer(transaction):
    msg = messages.SymbolTransfer()

    #TODO: SYMBOL DEBUG
    print("!!!!!!!!!!!!!!!!!!!!!!" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(transaction["mosaics"])
    print("!!!!!!!!!!!!!!!!!!!!!!" + "!!!!!!!!!!!!!!!!!!!!!!!!!!!!")

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


def fill_transaction_by_type(msg, transaction):
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
    else:
        raise ValueError("Unknown transaction type")


def create_sign_tx(transaction):
    msg = messages.SymbolSignTx()
    msg.transaction = create_transaction_common(transaction)

    fill_transaction_by_type(msg, transaction)

    return msg







# ====== Client functions ====== #

@expect(messages.SymbolSignedTx)
def sign_tx(client, n, transaction):
    try:
        msg = create_sign_tx(transaction)
    except ValueError as e:
        raise exceptions.TrezorException("Failed to encode transaction") from e

    assert msg.transaction is not None
    msg.transaction.address_n = n

    return client.call(msg)
