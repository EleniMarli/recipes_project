import pytest
from main.main_commands import from_filenames_to_temporary_shopping_list
from test.paths_config_for_tests import temporary_shopping_list_full_path, recipes_full_path, result_full_path


@pytest.mark.integration
def test_shopping_list_is_created_correctly():
    # given
    filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt']

    # when
    from_filenames_to_temporary_shopping_list(filenames_as_list_of_str, recipes_full_path, result_full_path)

    # then
    with open(temporary_shopping_list_full_path) as file:
        shopping_list = file.read()
        first_line = shopping_list.split('\n')[0]
        assert first_line == "Your shopping list:"
        assert "flour" in shopping_list
        assert "gelatin" in shopping_list