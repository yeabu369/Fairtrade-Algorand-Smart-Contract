from pyteal import *

from fairtrade_contract import Stage

if __name__ == "__main__":
    approval_program = Stage().approval_program()
    clear_program = Stage().clear_program()

    # Mode.Application specifies that this is a smart contract
    compiled_approval = compileTeal(approval_program, Mode.Application, version=6)
    print(compiled_approval)
    with open("fairtrade_approval.teal", "w") as teal:
        teal.write(compiled_approval)
        teal.close()

    # Mode.Application specifies that this is a smart contract
    compiled_clear = compileTeal(clear_program, Mode.Application, version=6)
    print(compiled_clear)
    with open("fairtrade_clear.teal", "w") as teal:
        teal.write(compiled_clear)
        teal.close()