#!/usr/bin/env python3
import argparse
import sys
from app import decode, encode, model

cipher_types = ['caesar', 'vigenere', 'vernam']


def add_encoding(subparsers):
    parser_encode = subparsers.add_parser('encode')
    parser_encode.add_argument('--cipher', choices=cipher_types)
    parser_encode.add_argument('--key')
    parser_encode.add_argument('--input-file', dest='input', default=sys.stdin)
    parser_encode.add_argument('--output-file', dest='output',
                               default=sys.stdout)
    parser_encode.set_defaults(func=encode.encode)


def add_decoding(subparsers):
    parser_decode = subparsers.add_parser('decode')
    parser_decode.add_argument('--cipher', choices=cipher_types)
    parser_decode.add_argument('--key')
    parser_decode.add_argument('--input-file', dest='input', default=sys.stdin)
    parser_decode.add_argument('--output-file', dest='output',
                               default=sys.stdout)
    parser_decode.set_defaults(func=decode.decode)


def add_train(subparsers):
    parser_train = subparsers.add_parser('train')
    parser_train.add_argument('--cipher', default='caesar')
    parser_train.add_argument('--text-file', dest='input')
    parser_train.add_argument('--model-file', dest='model')
    parser_train.set_defaults(func=model.train)


def add_hack(subparsers):
    parser_hack = subparsers.add_parser('hack')
    parser_hack.add_argument('--input-file', dest='input', default=sys.stdin)
    parser_hack.add_argument('--output-file', dest='output',
                             default=sys.stdout)
    parser_hack.add_argument('--model-file', dest='model')
    parser_hack.add_argument('--cipher', default='caesar')
    parser_hack.set_defaults(func=model.hack)


def main():
    parser = argparse.ArgumentParser(
        description='This program can encode, decode and hack simple ciphers',
        prog='cipher')
    subparsers = parser.add_subparsers()
    add_decoding(subparsers)
    add_encoding(subparsers)
    add_hack(subparsers)
    add_train(subparsers)
    args = parser.parse_args(sys.argv[1:])
    args.func(args)



if __name__ == '__main__':
    main()

