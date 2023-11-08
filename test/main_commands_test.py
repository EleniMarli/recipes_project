import pytest
import os

from main.shopping_list_module import Shopping_list
from main.main_commands import choose_files, from_filenames_to_temporary_shopping_list, execute_app
from test.paths_config_for_tests import temporary_shopping_list_full_path, recipes_full_path, result_full_path, permanent_result_folder_full_path



@pytest.mark.parametrize("user_input, expected_result", 
                         [('4 2', ['recipe4.txt', 'recipe2.txt']),
                          ('1', ['recipe1.txt']),
                          ('3 2 1', ['recipe3.txt', 'recipe2.txt', 'recipe1.txt'])])
def test_choose_files_works_with_valid_input(monkeypatch, user_input, expected_result):
    # setup
    monkeypatch.setattr('builtins.input', lambda : user_input)

    # given
    all_filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt', 'recipe3.txt', 'recipe4.txt']

    # when
    result = choose_files(all_filenames_as_list_of_str)

    # then
    assert result == expected_result



def test_choose_files_loops_for_invalid_input_type(monkeypatch):
    # setup
    user_input = iter(['-12', '0', 'yes', '345', '4'])
    monkeypatch.setattr('builtins.input', lambda : next(user_input))

    # given
    all_filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt', 'recipe3.txt', 'recipe4.txt']

    # when
    result = choose_files(all_filenames_as_list_of_str)

    # then
    assert result == ['recipe4.txt']



def test_choose_files_loops_for_invalid_numeric_input(monkeypatch):
    # setup
    user_input = iter(['5', '4'])
    monkeypatch.setattr('builtins.input', lambda : next(user_input))

    # given
    all_filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt', 'recipe3.txt', 'recipe4.txt']

    # when
    result = choose_files(all_filenames_as_list_of_str)

    # then
    assert result == ['recipe4.txt']



@pytest.mark.integration
def test_temporary_shopping_list_file_is_created_correctly():
    # given
    filenames_as_list_of_str = ['recipe1.txt', 'recipe2.txt']

    # when
    shopping_list = from_filenames_to_temporary_shopping_list(filenames_as_list_of_str, recipes_full_path, result_full_path)

    # then
    assert isinstance (shopping_list, Shopping_list)
    with open(temporary_shopping_list_full_path) as file:
        shopping_list_read = file.read()
        first_line = shopping_list_read.split('\n')[0]
        assert first_line == "Your shopping list:"
        assert "spaghetti" in shopping_list_read
        assert "Pecorino" in shopping_list_read
        assert "vanilla" in shopping_list_read