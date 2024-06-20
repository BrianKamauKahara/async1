from pydantic import BaseModel

class Page(BaseModel):
    number: int
    text: str

class Book(BaseModel):
    author: str
    title: str
    pages: list[Page]

my_books = [
		Book(
		    author="J. K. Rowling",
		    title="Harry Potter and the Philosopher's stone",
		    pages=[
		        Page(
		            number=1,
		            text="There once was a boy...",
		        ),
		        Page(
		            number=2,
		            text="He went to magic school...",
		        )
		    ]
		),
		Book(
		    author="Roger Zelazny",
		    title="Lord of Light",
		    pages=[
		        Page(
		            number=1,
		            text="It is said that fifty-three years ago...",
		        )
		    ]
		),
		Book(
            author="Gloria Mwaniga",
            title="Boyi",
            pages=[
		        Page(
		            number=1,
		            text="Madness entered Mama's eyes the day Baba pushed my brother Boyi to Matwa Kei and said.."
                    )
            ]
        )
]