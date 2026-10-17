# Ödev 1 kontrolü: odev1.py'yi çalıştırır, her görevin çıktısını beklenen çıktıyla karşılaştırır.
# PyCharm'da bu dosyayı açıp Run deyin. odev1.py ile aynı klasörde olmalı. Not vermez, yol gösterir.
import pathlib
import re
import subprocess
import sys

HERE = pathlib.Path(__file__).resolve().parent
ODEV = HERE / "odev1.py"

EXPECTED = {
    "1. Not kartı": ["Hacettepe Üniversitesi", "Not Döküm Belgesi (örnek)",
                     "Dersler: MAT123, FIZ127, TKD103", "Toplam kredi: 9"],
    "2. Hatalı satırlar": ["Ders 1 bitti", "IEEE Hacettepe", "Ankara'da 2026"],
    "3. Bir milyon saniye": ["Gün: 11.574074074074074", "11 gün 13 saat 46 dakika 40 saniye"],
    "4. AGNO'ya bir ders eklemek": ["Toplam kredi: 9", "AGNO: 2.9444444444444446", "BBM101 eklendi",
                                    "Toplam kredi: 12", "AGNO: 3.0833333333333335",
                                    "<class 'int'> <class 'float'>"],
    "5. Dört tane 4": ["1", "5", "6", "7"],
}
OPTIONAL = {"Meraklısına": ["Sonuç: 5.0", "Sonuç: 0.0", "Sonuç: 5"]}


def sections(text):
    """'=== başlık ===' satırlarına göre çıktıyı böler."""
    out, cur = {}, None
    for line in text.splitlines():
        m = re.fullmatch(r"=== (.+) ===", line.strip())
        if m:
            cur = m.group(1)
            out[cur] = []
        elif cur is not None:
            out[cur].append(line.rstrip())
    return out


def block(src, start, end):
    """odev1.py'de iki görev başlığı arasındaki kod (comment satırları hariç)."""
    a = src.find(start)
    b = src.find(end, a + 1) if end else len(src)
    lines = src[a:b if b != -1 else len(src)].splitlines()[1:]
    return [ln for ln in lines if ln.strip() and not ln.strip().startswith("#")]


def main():
    if not ODEV.exists():
        print("odev1.py bulunamadı. kontrol.py ile aynı klasöre koyun.")
        return
    run = subprocess.run([sys.executable, str(ODEV)], capture_output=True, text=True, timeout=20)
    if run.returncode != 0:
        last = [ln for ln in run.stderr.splitlines() if ln.strip()]
        print("odev1.py çalışırken hata verdi. Error message'ın son satırı:")
        print("   ", last[-1] if last else "(boş)")
        print("Önce bu hatayı düzeltin, sonra kontrolü tekrar çalıştırın.")
        return
    got = sections(run.stdout)
    src = ODEV.read_text(encoding="utf-8")
    passed = 0
    for title, want in EXPECTED.items():
        have = got.get(title)
        if have is None:
            print(f"✗ {title}: başlık satırı çıktıda yok. Başlığı yazdıran print() satırını silmeyin.")
            continue
        notes = []
        if have != want:
            for i, w in enumerate(want):
                h = have[i] if i < len(have) else "(satır yok)"
                if h != w:
                    notes.append(f"{i + 1}. satır beklenen: {w!r}, sizinki: {h!r}")
                    break
            else:
                notes.append(f"beklenenden fazla satır var: {have[len(want)]!r}")
        if title.startswith("1."):
            code = "\n".join(block(src, 'print("=== 1.', 'print("=== 2.'))
            if not re.search(r"4\s*\+\s*3\s*\+\s*2", code):
                notes.append("9'u kendiniz yazmayın, 4 + 3 + 2 expression'ı hesaplasın")
        if title.startswith("2."):
            code = "\n".join(block(src, 'print("=== 2.', 'print("=== 3.'))
            if code.count("SyntaxError") < 2 or "NameError" not in code:
                notes.append("her düzelttiğiniz satırın sonuna hatanın adını comment olarak yazın")
        if title.startswith("5."):
            for ln in block(src, 'print("=== 5.', 'print("=== Meraklısına'):
                if ln.count("4") != 4:
                    notes.append(f"bu satırda tam dört tane 4 yok: {ln.strip()}")
                if re.search(r"(?<!/)/(?!/)", ln):
                    notes.append(f"/ yerine // kullanın: {ln.strip()}")
        if notes:
            print(f"✗ {title}")
            for n in notes:
                print("    " + n)
        else:
            print(f"✓ {title}")
            passed += 1
    for title, want in OPTIONAL.items():
        have = got.get(title, [])
        if have:
            print(("✓ " if have == want else "· ") + title + " (zorunlu değil)")
    print(f"\n{passed} / {len(EXPECTED)} görev geçti.")


main()
