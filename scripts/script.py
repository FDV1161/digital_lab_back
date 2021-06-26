# ПЕРВЫЙ СПОСОБ
import sys
deviceFunctionId = sys.argv[1]
value = sys.argv[2]
print(deviceFunctionId, value)

# ВТОРОЙ СПОСОБ
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('deviceFunction', type=int)
parser.add_argument('value', type=int)
args = parser.parse_args()
print(args.deviceFunction, args.value)

