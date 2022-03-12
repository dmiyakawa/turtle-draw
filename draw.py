#!/usr/bin/env python3

import sys
import turtle


def parse_command(command_str):
    if ";" in command_str:
        # 本問の命令列を解釈する
        return [(elem[0], int(elem[1:])) for elem in command_str.split(";")]
    else:
        # 追加問題の命令列を解釈する
        commands = []
        prev_ch = None
        prev_index = None
        for index, ch in enumerate(command_str):
            if ch in "0123456789-":
                assert prev_ch is not None
                if prev_index is None:
                    prev_index = index
            else:
                assert ch in "FTRE"
                if prev_ch:
                    commands.append((prev_ch, int(command_str[prev_index:index])))
                prev_ch = ch
                prev_index = None
        if prev_ch:
            commands.append((prev_ch, int(command_str[prev_index:])))
        return commands


def run_commands(commands):
    opcode_index = 0
    stack = []
    while opcode_index < len(commands):
        current_command = commands[opcode_index]
        if current_command[0] == "F":
            turtle.forward(current_command[1])
        elif current_command[0] == "T":
            turtle.left(current_command[1])
        elif current_command[0] == "R":
            remaining = current_command[1]
            assert remaining > 0
            stack.append((opcode_index, remaining))
        elif current_command[0] == "E":
            loop_top_opcode_index, remaining = stack.pop()
            remaining -= 1
            if remaining > 0:
                stack.append((loop_top_opcode_index, remaining))
                opcode_index = loop_top_opcode_index
        else:
            raise RuntimeError(f"Unexpected code {current_command} in opcode {opcode_index}")
        opcode_index += 1


def main():
    if len(sys.argv) < 1:
        print(f"Usage: {sys.argv[0]} command", file=sys.stderr)
        return 1
    commands = parse_command(sys.argv[1])
    print(commands, file=sys.stderr)
    run_commands(commands)
    # これがないと、描画直後に画面が消えてしまい、スクリーンショットを撮ることができません :-)
    turtle.exitonclick()
    # 以下のようにしてももちろん良いです
    # print("Finished. Waiting for 10sec")
    # import time
    # time.sleep(10)
    return 0


if __name__ == "__main__":
    sys.exit(main())

