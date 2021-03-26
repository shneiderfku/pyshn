from pyshn.cnpj import cnpj, CnpjError
import pytest

def test_cnpj_repr():
    assert repr(cnpj(191)) == "<cnpj 00000000000191>"

def test_cnpj_str():
    assert str(cnpj("00.000.000/0001-91")) == "00.000.000/0001-91"

def test_cnpj_int():
    assert int(cnpj(191)) == 191

def test_cnpj_bool():
    assert bool(cnpj(191, validate=False)) == True
    assert bool(cnpj(190, validate=False)) == False

def test_cnpj_from_number():
    assert repr(cnpj(191)) == "<cnpj 00000000000191>"

def test_cnpj_generate_from_number():
    assert repr(cnpj(1, generate=True)) == "<cnpj 00000000000191>"

def test_cnpj_from_string():
    assert repr(cnpj("00000000000191")) == "<cnpj 00000000000191>"
    assert repr(cnpj("00.000.000/0001-91")) == "<cnpj 00000000000191>"

def test_cnpj_generate_from_string():
    assert repr(cnpj("000000000001", generate=True)) == "<cnpj 00000000000191>"
    assert repr(cnpj("00.000.000/0001", generate=True)) == "<cnpj 00000000000191>"

def test_cnpj_invalid_argument():
    with pytest.raises(TypeError, match="cnpj: must be number or string, not '?'."):
        cnpj([])
    with pytest.raises(TypeError, match="cnpj: must be number or string, not '?'."):
        cnpj(())

def test_cnpj_invalid_format():   
    with pytest.raises(CnpjError, match="invalid format '?'."):
        cnpj("00?000.000/0001-91")
    with pytest.raises(CnpjError, match="invalid format '?'."):
        cnpj("00.000?000/0001-91")
    with pytest.raises(CnpjError, match="invalid format '?'."):
        cnpj("00.000.000?0001-91")
    with pytest.raises(CnpjError, match="invalid format '?'."):
        cnpj("00.000.000/0001?91")

def test_cnpj_invalid_number():
    with pytest.raises(CnpjError, match="invalid number '?'"):
        cnpj("00.000.000/0001-90")

def test_cnpj_format():
    assert format(cnpj(191)) == "00.000.000/0001-91"
    assert format(cnpj(191), 's') == "00.000.000/0001-91"
    assert format(cnpj(191), 'n') == "00000000000191"
