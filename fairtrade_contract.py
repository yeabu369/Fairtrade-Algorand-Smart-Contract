from pyteal import *


class Stage:
    class Variables:
        title = Bytes("TITLE")
        summary = Bytes("SUMMARY")
        batch = Bytes("BATCH")
        attachment = Bytes("ATTACHMENT")

    def application_creation(self):
        return Seq([
            Assert(Txn.application_args.length() == Int(4)),
            Assert(Txn.note() == Bytes("fairtrade:uv1")),
            App.globalPut(self.Variables.title, Txn.application_args[0]),
            App.globalPut(self.Variables.summary, Txn.application_args[1]),
            App.globalPut(self.Variables.batch, Txn.application_args[2]),
            App.globalPut(self.Variables.attachment, Txn.application_args[3]),
            Approve()
        ])

    def application_deletion(self):
        return Return(Txn.sender() == Global.creator_address())

    def application_start(self):
        return Cond(
            [Txn.application_id() == Int(0), self.application_creation()],
            [Txn.on_completion() == OnComplete.DeleteApplication, self.application_deletion()]
        )

    def approval_program(self):
        return self.application_start()

    def clear_program(self):
        return Return(Int(1))
