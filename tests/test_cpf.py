from pyshn.cpf import cpf, CpfError
import pytest

def test_cpf_generate_from_number():
    assert repr(cpf(1, generate=True)) == "<cpf 00000000191>"

def test_cpf_from_number():
    assert repr(cpf(191)) == "<cpf 00000000191>"

def test_cpf_generate_from_string():
    assert repr(cpf("000000001", generate=True)) == "<cpf 00000000191>"
    assert repr(cpf("000.000.001", generate=True)) == "<cpf 00000000191>"

def test_cpf_from_string():
    assert repr(cpf("00000000191")) == "<cpf 00000000191>"
    assert repr(cpf("000000001/91")) == "<cpf 00000000191>"
    assert repr(cpf("000.000.001-91")) == "<cpf 00000000191>"

def test_cpf_invalid():
    with pytest.raises(TypeError, match="argument must be number or string, not '?'."):
        cpf([])
    with pytest.raises(TypeError, match="argument must be number or string, not '?'."):
        cpf(())
    with pytest.raises(CpfError, match="invalid number '?'."):
        cpf("000.000.001-00")
    with pytest.raises(CpfError, match="invalid format '?'."):
        cpf("000000001?00")
    with pytest.raises(CpfError, match="invalid format '?'."):
        cpf("000?000.001-91")
    with pytest.raises(CpfError, match="invalid format '?'."):
        cpf("000.000?001-91")
    with pytest.raises(CpfError, match="invalid format '?'."):
        cpf("000.000.001?91")

def test_cpf_truthy():
    assert bool(cpf(191, validate=False)) == True
    assert bool(cpf(100, validate=False)) == False

def test_cpf_str():
    assert str(cpf("000.000.001-91")) == "000.000.001-91"

def test_cpf_int():
    assert int(cpf(191)) == 191

def test_cpf_format():
    assert format(cpf(191)) == "000.000.001-91"
    assert format(cpf(191), 'n') == "00000000191"
    assert format(cpf(191), 'N') == "000000001/91"