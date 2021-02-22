import pathlib
import tempfile

from dotfiles.logics import CommandLineHelper, ExitCode, Fvwm2, Gdb, Git, Option, TMux, Vim, Vimperator, Zsh


def _check_file_exist(target: pathlib.Path) -> None:
    assert target.exists(), f"{target} not found"
    assert target.stat().st_size > 0


def test_tmux() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=False)
        r = TMux(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".tmux.conf")
        assert r.run() == ExitCode.SKIP


def test_vimperatorrc() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=False)
        r = Vimperator(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".vimperatorrc")
        assert r.run() == ExitCode.SKIP


def test_gdb() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=True)
        r = Gdb(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".gdbinit")
        assert r.run() == ExitCode.SUCCESS


def test_fvwm2() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=True)
        r = Fvwm2(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".fvwm2rc")
        assert r.run() == ExitCode.SUCCESS


def test_git() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=False)
        r = Git(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".gitconfig")
        assert r.run() == ExitCode.SKIP


def test_zsh() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=True)
        r = Zsh(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".zshrc")
        _check_file_exist(option.dest_dir / ".zshenv")
        assert r.run() == ExitCode.SUCCESS


def test_vim() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=False)
        r = Vim(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".vimrc")
        _check_file_exist(option.dest_dir / ".vim")
        assert r.run() == ExitCode.SKIP


def test_command() -> None:
    with tempfile.TemporaryDirectory() as d:
        option = Option(dest_dir=pathlib.Path(d), overwrite=True)
        r = CommandLineHelper(option)
        assert r.run() == ExitCode.SUCCESS
        _check_file_exist(option.dest_dir / ".docker" / "cli-plugins" / "docker-buildx")
        assert r.run() == ExitCode.SUCCESS
