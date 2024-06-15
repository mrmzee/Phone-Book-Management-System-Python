import pytest
from project import load_contacts, save_contacts, add_contact, find_contact

def test_load_contacts():
    """Tests the load_contacts function."""
    contacts = load_contacts("test_contacts.json")
    assert isinstance(contacts, list)

def test_save_contacts():
    """Tests the save_contacts function."""
    test_contacts = [{
        "name": "Alice",
        "phone": "123456",
        "last_name": "Smith",
        "age": "30",
        "country": "USA"
    }]
    save_contacts(test_contacts, "test_contacts.json")
    contacts = load_contacts("test_contacts.json")
    assert contacts == test_contacts

def test_add_contact():
    """Tests the add_contact function."""
    add_contact("Bob", "7891011", "Brown", "25", "Canada", "test_contacts.json")
    contacts = load_contacts("test_contacts.json")
    assert any(contact["name"] == "Bob" and contact["phone"] == "7891011" and contact["last_name"] == "Brown"
               and contact["age"] == "25" and contact["country"] == "Canada" for contact in contacts)

def test_find_contact():
    """Tests the find_contact function."""
    add_contact("Charlie", "5555555", "Johnson", "40", "UK", "test_contacts.json")
    contact = find_contact("5555555", "test_contacts.json")
    assert contact is not None
    assert contact["name"] == "Charlie"
    assert contact["phone"] == "5555555"
    assert contact["last_name"] == "Johnson"
    assert contact["age"] == "40"
    assert contact["country"] == "UK"
