import base64
import json
from pathlib import Path

NB_PATH = Path(__file__).parent.parent / "notebooks/01-eda.ipynb"
OUT_DIR = Path(__file__).parent.parent / "figures"

FIG_NAMES = {
    8: ["fig_histograms.png"],  # Distribución de las variables del estudio
    9: ["fig_scatter.png"],  # Distancia vs Duración
    11: ["fig_corr.png"],  # Matriz de correlación
    13: ["fig_dur_hour.png"],  # Duración mediana por hora de partida
    14: ["fig_dur_weekday.png"],  # Duración mediana por día de la semana
    16: ["fig_dur_geo.png"],  # Duración mediana según ubicación (recogida/llegada)
}


def main() -> None:
    with open(NB_PATH, encoding="utf-8") as f:
        nb = json.load(f)

    OUT_DIR.mkdir(exist_ok=True)
    exported = []

    for cell_id, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        pngs = [
            out["data"]["image/png"]
            for out in cell.get("outputs", [])
            if out.get("output_type") == "display_data"
            and "image/png" in out.get("data", {})
        ]
        names = FIG_NAMES.get(cell_id)
        if names is None:
            names = [f"fig_auto_{cell_id:02d}_{k}.png" for k in range(len(pngs))]

        for k, png in enumerate(pngs):
            if k >= len(names):
                names.append(f"fig_auto_{cell_id:02d}_{k}.png")
            path = OUT_DIR / names[k]
            with open(path, "wb") as img:
                img.write(base64.b64decode(png))
            exported.append(path.name)

    print(f"Exportadas {len(exported)} figuras a {OUT_DIR}/")
    for name in exported:
        print(f"  - {name}")


if __name__ == "__main__":
    main()
