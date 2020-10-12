import ast
import json
import rsa
import binascii
from Cryptodome.Signature import PKCS1_v1_5

#1 variant
def ENCRYPT_SENDER(Sender_public_key,msg):
    Message_b = msg.encode('utf-8')
    msg_from_sender = rsa.encrypt(Message_b, Sender_public_key)
    return str(msg_from_sender)

def ENCRYPT_RECIPIENT(Recipient_public_key, msg):
    Message_b = msg.encode('utf-8')
    msg_to_recipient = rsa.encrypt(Message_b, Recipient_public_key)
    return  str(msg_to_recipient)

def get_msg_with_decrypt():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
        private_key = keys[1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['recipient'] == public_key:
                    msg_encrypt = transactions['msg_to(recipient)']
                    msg_decrypt = rsa.decrypt(ast.literal_eval(msg_encrypt), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
                    return msg_decrypt.decode('utf-8')
                if transactions['sender'] == public_key:
                    msg_encrypt = transactions['msg_from(sender)']
                    msg_decrypt = rsa.decrypt(ast.literal_eval(msg_encrypt), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
                    return msg_decrypt.decode('utf-8')


def get_msg_sender():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['sender'] == public_key:
                    return transactions['msg']

def get_msg_recipient():
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        public_key = keys[0][:-1]
    with open('blockchain-5000.txt', 'r') as f:
        file_content = f.readlines()
        blockchain = json.loads(file_content[0][:-1])
        for block in blockchain[::-1]:
            for transactions in block['transactions']:
                if transactions['recipient'] == public_key:
                    return transactions['msg']

def DECRYPT_Sender(msg_decrypt):
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        private_key = keys[1]
    msg = get_msg_sender()
    msg_decrypted = rsa.decrypt(ast.literal_eval(msg), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
    return msg_decrypted

def DECRYPT_Recipient(msg_decrypt):
    with open('wallet-5000.txt', mode='r') as f:
        keys = f.readlines()
        private_key = keys[1]
    msg = get_msg_recipient()
    msg_decrypted = rsa.decrypt(ast.literal_eval(msg), PKCS1_v1_5.new(RSA.importKey(binascii.unhexlify(wallet.private_key))))
    return msg_decrypted


def main():
    SPUBKEY = "30819f300d06092a864886f70d010101050003818d0030818902818100eba89faca7239a758e190a5e1b066697da6b6c56c1512aa7e44cb44fa64f36a4aea8b0292703d40fde9713791e9379967ce7bfc493f4729a9af39ca190f3c015f4ca7595c441b8e730d073140d0c2c142d1c0214fcec6848abff0f3d069206e54c5663ed3a393b4e6b65392bbe56adb8fdee3e73f038cca25e74114679fcba170203010001"
    RPUBKEY = "30819f300d06092a864886f70d010101050003818d0030818902818100d61942583508341858b93d85957a1401855008d5c0e0d1b8fe0c5918ed0129b5b4c4c5ea4c9c0aaebbdb129e9ad35b50a4e579be57b713b0f6d276a18b15252b6db34cebc704cb147328aabf8ae4dbd8bd68be3c6f073cc012d1c0d40aaab1a923f7182bb371a0fff7caa96ce7facae74017b07b397bdc836bedf29c56cd986f0203010001"
    SPRIVKEY = "3082025c02010002818100eba89faca7239a758e190a5e1b066697da6b6c56c1512aa7e44cb44fa64f36a4aea8b0292703d40fde9713791e9379967ce7bfc493f4729a9af39ca190f3c015f4ca7595c441b8e730d073140d0c2c142d1c0214fcec6848abff0f3d069206e54c5663ed3a393b4e6b65392bbe56adb8fdee3e73f038cca25e74114679fcba17020301000102818008c3c9488d20dc5e51ee297e0d8843e992f49adf712a39296c6ad3ec007602c4c6403ce912ebe807bd122665c356ddd75486f411762549dbe9367555670441d91ceccd0a2f0d8884c0ad758a0ceaaabd11db25990fbac2052ff8b62223118dcd7baf6c3e4a2b91a1e915870782043df2ce5d0beb042a51fb6bc51dc0c8749325024100ece9b320bac26c5dce69439c11e9d74cfdac9b21342c7313cef0a00b9a6067c3ed2b1b3d1daa47aa0eb4091a031e3d5afce46ec84114a1ea97194f9b05ff47f3024100fea50e646eede22b0cfeb6f3640829d9a8ed552e5aa640b9c6395388e345da4182c85b77177ac148cf3aa7883f795934393e159c72593de988ceceb41887124d02407428bdb84d79a872721330a0243458691a73f7f7d6c1f8867ccf84594c0efab198e6aacb53713b0409838276eb927718d6a8161d3fb3a3140793d47139068abb0240545cba77eb8843f59f4883b3fedff57d76c9a9fec16972e81913c4e904e28f7c44a7bc25a851b2d73c5062507136f2a6aa9036f8ada983296b79986171fecdc1024100e8d53d288ee21f8ca3f832f05fe34dad4f7cd8874b71aafb3f1e9e31fc9d6df25f258405d6f7ea6a7ef54f25cca6616867d2b2fdb83c61bbee32f48406233f7b"
    RPRIVKEY = "3082025b02010002818100d61942583508341858b93d85957a1401855008d5c0e0d1b8fe0c5918ed0129b5b4c4c5ea4c9c0aaebbdb129e9ad35b50a4e579be57b713b0f6d276a18b15252b6db34cebc704cb147328aabf8ae4dbd8bd68be3c6f073cc012d1c0d40aaab1a923f7182bb371a0fff7caa96ce7facae74017b07b397bdc836bedf29c56cd986f020301000102818003100a706b95c9f4fd33ed2adf8807083c89780ee2baf495126147d700f0eed1501c2e7e9b08f2682c7cc647e98c1376d45d0a004c8dec64b02b33923d0498eafee875057e8864747d5478bc7dbb760707993d652ba90ef53a8b46d81cf6ce9fde02979399f8b9914b8f9710a1521bfabb0a6ebfa7726d1db9dd42edaf6fd439024100da821dec9c7f3fd1a80d43656c57759baa2a433a1cef3652253330515e88934b6405b9a885ee9e6b9d62b22eb10c1eb860bbf3c27173f885447fcf67c1e26b27024100fad573d2a4342c67088ec19c58ba855ee6a91d5f25ee59a2e71076bc57811f2346d950ce64fde11f95029faa3e6052a9336b1620a13bc18b78abc548f643557902401531115de53fa21cdf438a09c81c2357d98507c8170e4c226361378a6cb4aa34619afc8a8f92b8e28efd0772e7d0d919e0a7d9d83dd09585b742fe067e134b7902406e667684f6aad404415afbd241a74ebe574d85d4f40ff539e2f3771f2c7073710664edd0f9d858369b523d4e24082739bb9cdd6f5d27bce713249f3f9ecc4219024056732a4fb11c47f0d5e1d4cbd5931833033c2cf11c63deb6bac08960ec82ffca29285f07cfd32088cc265fdaac81f833a76dd489826c425fe6682a23699f1012"
    msg = input()
    encrypted1 = ENCRYPT_SENDER(SPUBKEY, msg)
    print(encrypted1)
    decrypted1 = DECRYPT_Sender(SPRIVKEY, msg)
    print(decrypted1)
    encrypted2 = ENCRYPT_RECIPIENT(RPUBKEY, msg)
    print(encrypted2)
    decrypted2 = DECRYPT_Recipient(RPRIVKEY, msg)
    print(decrypted2)

if __name__ == "__main__":
    main()