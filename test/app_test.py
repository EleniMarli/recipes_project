import pytest
from main.main_commands import from_filenames_to_shopping_list

@pytest.mark.integration
def test_shopping_list_is_created_correctly():
    # given
    text_folder_path = 'C:/VSCode/recipes_project/test/text'
    recipes_path = text_folder_path + '/recipes'
    result_path = text_folder_path + '/result'
    filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt']

    # when
    from_filenames_to_shopping_list(filenames_as_list_of_str, recipes_path, result_path)

    # then
    with open(f"C:/VSCode/recipes_project/test/text/result/myshoppinglist.txt") as file:
        shopping_list = file.read()
        first_line = shopping_list.split('\n')[0]
        assert first_line == "Your shopping list:"
        assert "flour" in shopping_list
        assert "gelatin" in shopping_list