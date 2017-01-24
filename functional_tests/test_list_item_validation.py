from . base import FunctionalTest


class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes to the home page and accidentally tries to submit
        # and empty list item. She hits Enter on the empty input box

        # The home page refreshes, and there is an error message saying
        # that list items cannot be blank

        # She tries again with osme text for the item, which now works

        # Perversly, she now decides to submit a second blank list item

        # She recieves a similar warining on the list page

        # And she can correct it by filling some text in
        self.fail('write me!')
