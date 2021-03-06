from .. import ipcrpc
import sys
import traceback


def main() -> int:
    exit_code = 0
    try:
        client = ipcrpc.RpcClient(verbose=True)
        client.eth_coinbase()
        client.send_rpc('eth_getBlockByNumber', 815859, False)
    
        for i in range(10):
            client.eth_getBlockByNumber(i, False, batch=True)
        client.send_batch()
    except Exception as exc:
        traceback.print_exc()
        exit_code = 1
    finally:
        return exit_code

if __name__ == '__main__':
    sys.exit(main())
