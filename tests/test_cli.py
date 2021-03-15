from click.testing import CliRunner
from pyshn.cli import main
import pytest

def test_pyshn_cpf():
    runner = CliRunner()
    result = runner.invoke(main, ['cpf', '191'])
    assert result.exit_code == 0
    assert result.output == '000.000.001-91 (valid)\n'

def test_pyshn_cpf_format():
    runner = CliRunner()
    with runner.isolation():
        result = runner.invoke(main, ['cpf', '--format', 's', '191'])
        assert result.exit_code == 0
        assert result.output == '000.000.001-91 (valid)\n'
    with runner.isolation():
        result = runner.invoke(main, ['cpf', '--format', 'n', '191'])
        assert result.exit_code == 0
        assert result.output == '00000000191 (valid)\n'
    with runner.isolation():
        result = runner.invoke(main, ['cpf', '--format', 'N', '191'])
        assert result.exit_code == 0
        assert result.output == '000000001/91 (valid)\n'

def test_pyshn_cpf_no_validate():
    runner = CliRunner()
    with runner.isolation():
        result = runner.invoke(main, ['cpf', '--no-validate', '191'])
        assert result.exit_code == 0
        assert result.output == '000.000.001-91\n'
    with runner.isolation():
        result = runner.invoke(main, ['cpf', '--no-validate', '1'])
        assert result.exit_code == 0
        assert result.output == '000.000.000-01\n'

def test_pyshn_cpf_generate():
    runner = CliRunner()
    result = runner.invoke(main, ['cpf', '--generate', '1'])
    assert result.exit_code == 0
    assert result.output == '000.000.001-91\n'

def test_pyshn_cpf_invalid_format():
    runner = CliRunner()
    result = runner.invoke(main, ['cpf', 'x'])
    assert result.exit_code == 0
    assert result.output == "pyshn: invalid format 'x'.\n"
