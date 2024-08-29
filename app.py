from fasthtml.common import * 

app = FastHTML(hdrs=Link(rel="stylesheet", href="app.css", type="text/css")) 
rt = app.route

def inputField(i, val=None):
    return Input(type="text", maxlength=1, id=i, value=val, cls="text-center bg-white border-2 border-black rounded-md p-2 text-lg font-mono uppercase w-[44px]")

inputWord = Form(
        inputField("input1"),
        inputField("input2"),
        inputField("input3"),
        inputField("input4"),
        inputField("input5"),
        Input(type="hidden", id="combinedInput", name="word"),
        Script("""
            document.getElementById('wordForm').addEventListener('submit', function(event) {
                const inputs = [
                    document.getElementById('input1').value,
                    document.getElementById('input2').value,
                    document.getElementById('input3').value,
                    document.getElementById('input4').value,
                    document.getElementById('input5').value
                ];
                document.getElementById('combinedInput').value = inputs.join('');
            });
        """),
        Button("Submit", cls="px-2 border-2 border-black rounded-md bg-[#f5004f]"),
        hx_post="/submit",
        hx_target="#input1",
        target_id="input1",
        hx_swap="outerHTML",
        cls="flex flex-row"
)


@dataclass
class Word:
    input1: str;
    input2: str;
    input3: str;
    input4: str;
    input5: str;

@rt("/{fname:path}.{ext:static}")
def get(fname:str, ext:str): 
    return FileResponse(f'public/{fname}.{ext}')

@rt('/')
def get():
    return Div(Head(Title("Wordle")), 
    Body(
        Div(
            H1("Wordle", cls="text-[#ffaf00] text-[60px]"),
            H3("Start guessing by entering a 5 letter word", cls="my-4 text-white text-lg"),
            Div(
                inputWord,
                inputWord,
                inputWord,
                inputWord,
                inputWord,
                cls="p-2 flex flex-col space-y-2"
            ),
           cls="p-10 flex flex-col justify-center items-center"
        ), cls="bg-[#7c00fe]")
    ) 

@rt('/submit')
def post(word: Word):
    return inputField("input1", word.input1) 

serve()