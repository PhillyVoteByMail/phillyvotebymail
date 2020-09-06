"""
Generates tables from a yaml schema
"""
import os
import yaml
from typing import List

from sqlalchemy import Table, MetaData, Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import mapper
from .base import Base
from ..schemas import Schema


def create_class_from_schema(class_name: str, table_name: str, schema: Schema, base_class=Base):
    schema_fields = schema.fields
    class_attrs = {
        "__tablename__": table_name,
    }

    for field in schema_fields:
        column_name = field['field']
        primary_key = column_name == schema.primary_key_name
        column_type_str = field['type']
        column_type = String(100)
        if column_type_str == 'Date':
            column_type = Date()
        class_attrs[field['field']] = Column(column_name, column_type, primary_key=primary_key)
    
    return type(class_name, (base_class, ), class_attrs)
