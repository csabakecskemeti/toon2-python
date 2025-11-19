#!/usr/bin/env python3
"""
Fixed Test Data and Questions - Restoring Original Working Simple Tests + Adding Complex Ones
"""

import requests
from typing import Dict, List, Any, Tuple, Optional
from dataclasses import dataclass


@dataclass
class TestCase:
    name: str
    data: Any
    questions: List[str]
    expected_types: List[str]
    complexity_level: str = 'simple'


def fetch_dummyjson_data(endpoint: str, limit: int = 8) -> Optional[Dict]:
    """Fetch data from dummyjson.com API with error handling."""
    try:
        response = requests.get(f'https://dummyjson.com/{endpoint}?limit={limit}', timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"  ⚠️  API fetch failed: {e}")
        return None


def generate_comprehensive_test_cases() -> List[TestCase]:
    """
    Generate test cases including:
    1. Original 16 simple questions that were working perfectly (100% success)
    2. Additional complex analytical questions for deeper testing
    """
    test_cases = []
    
    # ============================================================================
    # ORIGINAL WORKING SIMPLE TESTS (that achieved 100% success rate)
    # ============================================================================
    
    # 1. User Demographics (Real DummyJSON data) - 4 questions
    users_data = fetch_dummyjson_data('users', 8)
    if users_data:
        test_cases.append(TestCase(
            name="User Demographics",
            data=users_data,
            questions=[
                "Find the user with id=3 and provide only their exact 'address.city' value.",
                "Look at all users and find the one with the longest 'firstName' (most characters). Provide only that person's exact 'firstName'.",
                "Find the user whose 'company.title' contains the word 'Manager' and provide only their exact 'lastName'.",
                "Look at the 'userAgent' fields and find which one mentions 'Chrome'. Provide only the exact 'username' of that user."
            ],
            expected_types=['text', 'text', 'text', 'text'],
            complexity_level='simple'
        ))
    
    # 2. Product Catalog (Real DummyJSON data) - 4 questions
    products_data = fetch_dummyjson_data('products', 6)
    if products_data:
        test_cases.append(TestCase(
            name="Product Catalog",
            data=products_data,
            questions=[
                "Find the product with id=7 and provide only its exact 'brand' value.",
                "Look at all product descriptions and find which one mentions the word 'skin'. Provide only that product's exact 'title'.",
                "Find the product that has 'moisturizing' in its description and provide only its exact 'category' value.",
                "Look at the 'tags' arrays and find a product that has 'lipstick' as one of its tags. Provide only that product's exact 'brand' value."
            ],
            expected_types=['text', 'text', 'text', 'text'],
            complexity_level='simple'
        ))
    
    # 3. E-commerce Orders (Complex synthetic data) - 4 questions
    orders_data = {
        "orders": [
            {
                "id": "ORD-001",
                "customer": {"name": "Alice Johnson", "city": "NYC", "age": 28},
                "items": [
                    {"product": "Laptop", "price": 999.99, "qty": 1, "category": "Electronics"},
                    {"product": "Mouse", "price": 29.99, "qty": 2, "category": "Electronics"}
                ],
                "totals": {"subtotal": 1059.97, "tax": 84.80, "shipping": 15.00, "total": 1159.77},
                "date": "2025-01-15"
            },
            {
                "id": "ORD-002", 
                "customer": {"name": "Bob Smith", "city": "LA", "age": 35},
                "items": [
                    {"product": "Book", "price": 19.99, "qty": 3, "category": "Books"},
                    {"product": "Bookmark", "price": 4.99, "qty": 1, "category": "Books"}
                ],
                "totals": {"subtotal": 64.96, "tax": 5.20, "shipping": 5.00, "total": 75.16},
                "date": "2025-01-16"
            },
            {
                "id": "ORD-003",
                "customer": {"name": "Carol Brown", "city": "NYC", "age": 42},
                "items": [
                    {"product": "Tablet", "price": 299.99, "qty": 1, "category": "Electronics"},
                    {"product": "Case", "price": 24.99, "qty": 1, "category": "Electronics"}
                ],
                "totals": {"subtotal": 324.98, "tax": 26.00, "shipping": 10.00, "total": 360.98},
                "date": "2025-01-17"
            }
        ]
    }
    
    test_cases.append(TestCase(
        name="E-commerce Orders",
        data=orders_data,
        questions=[
            "Find the order with id='ORD-002' and provide only the exact 'customer.name' value.",
            "Look at all items across all orders and find one that has 'Book' as its product name. Provide only the exact order 'id' that contains this item.",
            "Find the customer who lives in 'LA' and provide only their exact 'age' value.",
            "Look at all orders and find which one has a 'date' of '2025-01-17'. Provide only the exact 'customer.city' of that order."
        ],
        expected_types=['text', 'text', 'number', 'text'],
        complexity_level='simple'
    ))
    
    # 4. Customer Reviews (Sentiment and content analysis) - 4 questions
    reviews_data = {
        "reviews": [
            {
                "id": 1,
                "customer": "Alice",
                "product": "Laptop",
                "rating": 5,
                "comment": "This laptop is absolutely amazing! Fast, reliable, and beautiful design. I love it!",
                "date": "2025-01-10"
            },
            {
                "id": 2,
                "customer": "Bob",
                "product": "Headphones",
                "rating": 2,
                "comment": "Terrible sound quality. Very disappointed and frustrated with this purchase. Would not recommend.",
                "date": "2025-01-11"
            },
            {
                "id": 3,
                "customer": "Carol",
                "product": "Mouse",
                "rating": 4,
                "comment": "Pretty good mouse overall. Works well but could be more ergonomic. Happy with it.",
                "date": "2025-01-12"
            },
            {
                "id": 4,
                "customer": "David",
                "product": "Keyboard",
                "rating": 1,
                "comment": "Awful product! Keys are sticky and it broke after one week. Worst purchase ever!",
                "date": "2025-01-13"
            }
        ]
    }
    
    test_cases.append(TestCase(
        name="Customer Reviews",
        data=reviews_data,
        questions=[
            "Read all review comments and find the one that sounds most negative or angry. Provide only the exact 'customer' name who wrote that review.",
            "Find the review with id=3 and provide only the exact 'product' name that was reviewed.",
            "Look at all comments and find which one mentions the word 'ergonomic'. Provide only the exact 'rating' value of that review.",
            "Find the review that was posted on '2025-01-10' and provide only the exact 'product' name."
        ],
        expected_types=['text', 'text', 'number', 'text'],
        complexity_level='simple'
    ))
    
    # ============================================================================
    # ADDITIONAL COMPLEX ANALYTICAL TESTS (for deeper format evaluation)  
    # ============================================================================
    
    # 5. Advanced Analytics Test Case
    advanced_data = {
        "employees": [
            {"id": 1, "name": "Alice Chen", "age": 28, "department": "Engineering", "salary": 95000, "gender": "F", "hire_date": "2022-03-15"},
            {"id": 2, "name": "Bob Wilson", "age": 34, "department": "Marketing", "salary": 75000, "gender": "M", "hire_date": "2020-08-20"},
            {"id": 3, "name": "Carol Smith", "age": 29, "department": "Engineering", "salary": 88000, "gender": "F", "hire_date": "2021-11-10"},
            {"id": 4, "name": "David Brown", "age": 42, "department": "Sales", "salary": 82000, "gender": "M", "hire_date": "2019-05-03"},
            {"id": 5, "name": "Eva Rodriguez", "age": 31, "department": "Engineering", "salary": 92000, "gender": "F", "hire_date": "2020-12-01"}
        ]
    }
    
    test_cases.append(TestCase(
        name="Advanced Analytics",
        data=advanced_data,
        questions=[
            "Calculate the average salary of employees in the 'Engineering' department. Round to the nearest dollar and provide only the integer.",
            "Find the average salary of female employees between ages 25-35. Round to the nearest dollar and provide only the integer.",
            "Count how many employees work in each department. Format as 'Department: count' on separate lines.",
            "Find the department with the highest average salary. Provide only the exact department name."
        ],
        expected_types=['number', 'number', 'list', 'text'],
        complexity_level='complex'
    ))
    
    # ============================================================================
    # ADDITIONAL DATASETS FROM COMPREHENSIVE TEST (for fidelity/compression only)
    # ============================================================================
    
    # 6. Flat Object Array
    flat_data = {
        'items': [
            {'id': 1, 'name': 'Alice', 'age': 25, 'active': True},
            {'id': 2, 'name': 'Bob', 'age': 30, 'active': False},
            {'id': 3, 'name': 'Charlie', 'age': 35, 'active': True}
        ]
    }
    test_cases.append(TestCase(
        name="Flat Object Array",
        data=flat_data,
        questions=[], expected_types=[], complexity_level='simple'
    ))

    # 7. Single Level Nesting
    nested_data = {
        'users': [
            {
                'id': 1,
                'profile': {'name': 'Alice', 'email': 'alice@test.com'},
                'settings': {'theme': 'dark', 'notifications': True}
            },
            {
                'id': 2, 
                'profile': {'name': 'Bob', 'email': 'bob@test.com'},
                'settings': {'theme': 'light', 'notifications': False}
            }
        ]
    }
    test_cases.append(TestCase(
        name="Single Level Nesting",
        data=nested_data,
        questions=[], expected_types=[], complexity_level='simple'
    ))

    # 8. Deep Nesting (3+ levels)
    deep_nested_data = {
        'company': [
            {
                'id': 1,
                'name': 'TechCorp',
                'location': {
                    'address': {
                        'street': '123 Tech St',
                        'city': 'San Francisco',
                        'coordinates': {
                            'lat': 37.7749,
                            'lng': -122.4194,
                            'precision': {'meters': 10, 'confidence': 0.95}
                        }
                    },
                    'timezone': 'PST'
                },
                'departments': [
                    {
                        'name': 'Engineering',
                        'head': {
                            'name': 'Jane Doe',
                            'contact': {
                                'email': 'jane@techcorp.com',
                                'phone': {'office': '555-1234', 'mobile': '555-5678'}
                            }
                        }
                    }
                ]
            }
        ]
    }
    test_cases.append(TestCase(
        name="Deep Nesting",
        data=deep_nested_data,
        questions=[], expected_types=[], complexity_level='complex'
    ))

    # 9. Mixed Data Types
    mixed_data = {
        'records': [
            {
                'id': 1,
                'timestamp': '2024-01-01T10:00:00Z',
                'value': 42.5,
                'tags': ['urgent', 'customer'],
                'metadata': {
                    'source': 'api',
                    'version': 1.2,
                    'validated': True,
                    'errors': None
                }
            },
            {
                'id': 2,
                'timestamp': '2024-01-01T11:00:00Z', 
                'value': -15.8,
                'tags': ['normal', 'internal'],
                'metadata': {
                    'source': 'batch',
                    'version': 1.1,
                    'validated': False,
                    'errors': ['missing_field']
                }
            }
        ]
    }
    test_cases.append(TestCase(
        name="Mixed Data Types",
        data=mixed_data,
        questions=[], expected_types=[], complexity_level='complex'
    ))

    # 10. Sparse Data (lots of nulls)
    sparse_data = {
        'entries': [
            {
                'id': 1,
                'name': 'Complete',
                'email': 'complete@test.com',
                'phone': '555-1234',
                'address': {'street': '123 Main', 'city': 'NYC'}
            },
            {
                'id': 2,
                'name': 'Partial',
                'email': None,
                'phone': None,
                'address': {'street': None, 'city': 'LA'}
            },
            {
                'id': 3,
                'name': 'Minimal', 
                'email': None,
                'phone': None,
                'address': None
            }
        ]
    }
    test_cases.append(TestCase(
        name="Sparse Data",
        data=sparse_data,
        questions=[], expected_types=[], complexity_level='simple'
    ))

    # 11. Array of Primitives
    primitives_data = {
        'numbers': [1, 2, 3, 4, 5],
        'strings': ['apple', 'banana', 'cherry'],
        'booleans': [True, False, True],
        'mixed': [1, 'text', True, None, 3.14]
    }
    test_cases.append(TestCase(
        name="Array of Primitives",
        data=primitives_data,
        questions=[], expected_types=[], complexity_level='simple'
    ))

    # 12. Deeply Nested Arrays
    matrix_data = {
        'matrix': [
            [
                {'x': 0, 'y': 0, 'value': 1.0},
                {'x': 0, 'y': 1, 'value': 0.5}
            ],
            [
                {'x': 1, 'y': 0, 'value': 0.3},
                {'x': 1, 'y': 1, 'value': 0.8}
            ]
        ]
    }
    test_cases.append(TestCase(
        name="Deeply Nested Arrays",
        data=matrix_data,
        questions=[], expected_types=[], complexity_level='complex'
    ))
    
    return test_cases