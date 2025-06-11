from shiny import App, ui, render, reactive
from shinywidgets import output_widget, render_widget


zonas_horarias = {
    "America/Mexico_City": "CDMX",
    "America/Chihuahua": "Chihuahua",
    "America/Hermosillo": "Hermosillo ",
    "America/Cancun": "Cancún",
}

sun_path_ui = ui.page_fluid(
    ui.h2("Trayectoria solar interactiva"),
    ui.layout_sidebar(
        ui.sidebar(
            ui.input_numeric("lat", "Latitud:", value=18.85),
            ui.input_numeric("lon", "Longitud:", value=-99.22),
            ui.input_select("tz", "Zona horaria:", zonas_horarias),
            ui.input_radio_buttons("horario", "Horario:", {
                "civil": "Horario estándar (civil)",
                "solar": "Horario solar verdadero"
            }, selected="civil"),
            ui.input_radio_buttons("graficas", "Mostrar:", {
                "cartesiana": "Solo cartesiana",
                "polar": "Solo estereográfica",
                "ambas": "Ambas gráficas"
            }, selected="cartesiana"),
            ui.input_checkbox("ver_tabla_check", "Mostrar tabla de datos", False),
            ui.download_button("descargar_datos", "📥 Descargar datos")
        ),
        ui.div(
            output_widget("grafico_cartesiano"),
            output_widget("grafico_polar"),
            ui.output_ui("mostrar_tabla")
        )
    )
)