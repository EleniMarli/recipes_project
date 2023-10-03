import main.app # runs app script

def test_shopping_list_is_created_correctly():
    with open(f"C:/VSCode/recipes_project/main/text/result/myshoppinglist.txt") as file:
        shopping_list = file.read()
        first_line = shopping_list.split('\n')[0]
        assert first_line == "Your shopping list:"
        assert "flour" in shopping_list
        assert "sugar" in shopping_list