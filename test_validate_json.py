import pytest

from validate_json import validate_signals


def test_validate_signals_accepts_valid_definition():
    model = validate_signals(
        signal="aeb",
        SignalDatatype="int",
        SignalDefaulValue=23,
        BusSignal="AEB",
        BusSignalDatatype="int",
        BusSignalDefaulValue=23,
    )

    assert model.signal == "aeb"
    assert model.SignalDatatype == "int"
    assert model.SignalDefaulValue == 23
    assert model.BusSignal == "AEB"
    assert model.BusSignalDatatype == "int"
    assert model.BusSignalDefaulValue == 23


def test_validate_signals_rejects_invalid_datatype():
    with pytest.raises(ValueError, match="SignalDatatype must be one of"):
        validate_signals(
            signal="fcw",
            SignalDatatype="integer",
            SignalDefaulValue=0,
            BusSignal="FCW",
            BusSignalDatatype="int",
            BusSignalDefaulValue=0,
        )


def test_validate_signals_rejects_signal_default_type_mismatch():
    with pytest.raises(ValueError, match="SignalDefaulValue must match datatype int"):
        validate_signals(
            signal="ldw",
            SignalDatatype="int",
            SignalDefaulValue="1",
            BusSignal="LDW",
            BusSignalDatatype="int",
            BusSignalDefaulValue=1,
        )


def test_validate_signals_rejects_bus_default_type_mismatch():
    with pytest.raises(ValueError, match="BusSignalDefaulValue must match datatype bool"):
        validate_signals(
            signal="airbag",
            SignalDatatype="bool",
            SignalDefaulValue=True,
            BusSignal="AIRBAG",
            BusSignalDatatype="bool",
            BusSignalDefaulValue=1,
        )
