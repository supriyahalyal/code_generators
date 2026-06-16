from typing import Any

from pydantic import BaseModel, ValidationError, model_validator
import json
import logging

class validate_signals(BaseModel):
    signal: str
    SignalDatatype: str
    SignalDefaulValue: Any
    BusSignal: str
    BusSignalDatatype: str
    BusSignalDefaulValue: Any

    @model_validator(mode="after")
    def check_datatypes_and_defaults(self):
        valid_types = {
            "int": int,
            "float": (float, int),
            "bool": bool,
            "string": str,
        }

        for datatype_key, default_key in [
            ("SignalDatatype", "SignalDefaulValue"),
            ("BusSignalDatatype", "BusSignalDefaulValue"),
        ]:
            datatype = getattr(self, datatype_key)
            if datatype not in valid_types:
                raise ValueError(f"{datatype_key} must be one of {list(valid_types)}")

            default_value = getattr(self, default_key)
            expected_type = valid_types[datatype]
            if not isinstance(default_value, expected_type):
                raise ValueError(f"{default_key} must match datatype {datatype}")

        return self

class ReadValidateJson:
    def __init__(self):
        self.set_logging()

    def set_logging(self):
        self.logger = logging.getLogger(__name__)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime) - %(name)s - %(levelname)s- %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)

    def read_signals_json(self):
        file_path = "signals/signal_list.json"
        with open(file_path, "r", encoding="utf-8") as fp:
            self.signal_list =  json.load(fp)
        self.validate_signal_list()
        return self.signal_list


    def validate_signal_item(self, signal_data):
        return validate_signals(**signal_data)


    def validate_signal_list(self):
        try:
            [self.validate_signal_item(item) for item in self.signal_list]
        except (ValidationError, ValueError) as exc:
            print("Validation failed:", exc)


if __name__ == "__main__":
    signals = ReadValidateJson()
    print(signals.read_signals_json())
