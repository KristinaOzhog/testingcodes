import pytest
from secretary import show_all_docs_info, add_new_doc, delete_doc


def test_show_all_docs_info():
    assert show_all_docs_info() is None


def test_add_new_doc():
    assert add_new_doc('passport', '542164', 'Kristina Ozhog', '3')

    
def test_delete_doc():
    delete_doc('10006')