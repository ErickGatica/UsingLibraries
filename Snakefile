rule process:
    output:
        processed="Data/processed_data.csv"
    shell:
        "python3 process_data.py"

rule plots:
    input:
        processed="Data/processed_data.csv"
    output:
        plot="figures/4_panel_plot.png"
    shell:
        "python3 main.py"
    

