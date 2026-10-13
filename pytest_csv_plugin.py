
import csv
import os

import pytest


resultados = []


def pytest_runtest_logreport(report):
    # Guardar el resultado final de cada prueba.
    if report.when == "call" or (
        report.when == "setup"
        and report.outcome in ("failed", "skipped")
    ):
        if report.passed:
            estado = "PASSED"
        elif report.failed:
            estado = "FAILED"
        else:
            estado = "SKIPPED"

        detalle = ""
        if report.failed or report.skipped:
            detalle = str(getattr(report, "longreprtext", ""))

        resultados.append({
            "prueba": report.nodeid,
            "resultado": estado,
            "duracion_segundos": round(report.duration, 4),
            "detalle": detalle,
        })


def pytest_sessionfinish(session, exitstatus):
    os.makedirs("reports", exist_ok=True)

    ruta = os.path.join("reports", "pytest_results.csv")

    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        columnas = [
            "prueba",
            "resultado",
            "duracion_segundos",
            "detalle",
        ]

        escritor = csv.DictWriter(
            archivo,
            fieldnames=columnas,
        )
        escritor.writeheader()
        escritor.writerows(resultados)
