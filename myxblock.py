"""TO-DO: Write a description of what this XBlock is."""

from web_fragments.fragment import Fragment
from xblock.core import XBlock
from xblock.fields import Integer, Scope

class MyXBlock(XBlock):
    views = Integer(help="the number of times this block has been viewed", 
                    default=0, 
                    scope=Scope.user_state_summary)

    def student_view(self, context):
        """
        Render the block for students.
        """
        self.views += 1
        html = f"Hello this is my custom x block"
        frag = Fragment(html)
        return frag

    @staticmethod
    def workbench_scenarios():
        return [
            ("MyXBlock",
             """<myxblock/>
             """),
            ("Multiple MyXBlock",
             """<vertical_demo>
                <myxblock/>
                <myxblock/>
                <myxblock/>
                </vertical_demo>
             """),
        ]