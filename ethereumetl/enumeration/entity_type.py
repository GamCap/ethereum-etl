class EntityType:
    BLOCK = 'block'
    TRANSACTION = 'transaction'
    RECEIPT = 'receipt'
    LOG = 'log'
    ERC20_TRANSFER = 'erc20_transfer'
    ERC721_TRANSFER = 'erc721_transfer'
    TOKEN_TRANSFER = 'token_transfer'
    TRACE = 'trace'
    CONTRACT = 'contract'
    TOKEN = 'token'

    ALL_FOR_STREAMING = [BLOCK, TRANSACTION, LOG, ERC20_TRANSFER, ERC721_TRANSFER, TOKEN_TRANSFER, TRACE, CONTRACT, TOKEN]
    ALL_FOR_INFURA = [BLOCK, TRANSACTION, LOG, ERC20_TRANSFER, ERC721_TRANSFER, TOKEN_TRANSFER]
