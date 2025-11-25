import sys
from pathlib import Path

TEXT_EXTS = {
    '.py', '.js', '.css', '.html', '.htm', '.txt', '.md', '.json',
    '.yml', '.yaml', '.ini', '.cfg', '.conf', '.csv', '.tsv', '.xml', '.svg'
}

def to_crlf_bytes(data: bytes) -> bytes:
    # Normaliza primero a LF y luego a CRLF para evitar duplicados.
    return data.replace(b'\r\n', b'\n').replace(b'\n', b'\r\n')

def convert_tree(base: Path) -> int:
    changed = 0
    for p in base.rglob('*'):
        if not p.is_file():
            continue
        if p.suffix.lower() not in TEXT_EXTS:
            continue
        data = p.read_bytes()
        new_data = to_crlf_bytes(data)
        if new_data != data:
            p.write_bytes(new_data)
            changed += 1
    return changed

def main():
    # Intenta 'productionfiles' y, si no existe, 'my_tennis_club/productionfiles'.
    candidates = [Path('productionfiles'), Path('my_tennis_club') / 'productionfiles']
    base = next((c for c in candidates if c.is_dir()), None)
    if not base:
        print("No se encontró la carpeta 'productionfiles'. Ejecuta el script desde la raíz del repo.", file=sys.stderr)
        sys.exit(1)
    n = convert_tree(base)
    print(f'Archivos actualizados: {n}')

if __name__ == '__main__':
    main()
