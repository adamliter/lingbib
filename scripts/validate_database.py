#! /usr/bin/env python
import yaml
with open("database/src/database.yaml") as f:
    db = yaml.load(f)
with open("schema/lingbib.schema.yaml") as f:
    schema = yaml.load(f)

import jsonschema
jsonschema.validate(db, schema)
