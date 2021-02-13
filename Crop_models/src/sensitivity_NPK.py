def sensitivity_NPK(fertilizer):
    N_kg_local, P_kg_local, K_kg_local = fertilizer
    print('N:{N_kg},N:{P_kg},N:{K_kg}'.format(N_kg=N_kg_local, P_kg=P_kg_local, K_kg=K_kg_local))
    year_date=2019
    yaml_agro = f"""
    - {year_date}-06-01:
        CropCalendar:
            crop_name: 'sugar-beet'
            variety_name: 'sugar-beet-601'
            crop_start_date: {year_date}-06-02
            crop_start_type: emergence
            crop_end_date: {year_date}-10-15
            crop_end_type: harvest
            max_duration: 300
        TimedEvents:
        -   event_signal: apply_npk
            name:  Timed N/P/K application table
            comment: All fertilizer amounts in kg/ha
            events_table:
            - {year_date}-06-22: {{N_amount : {N_kg_local}, P_amount: {P_kg_local}, K_amount: {K_kg_local}}}
        StateEvents: null
    """
    agromanagement = yaml.load(yaml_agro)
    wofsim = Wofost71_WLP_FD(parameters, moscow_weather, agromanagement)
    wofsim.run_till_terminate()
    df_results = pd.DataFrame(wofsim.get_output())
    df_results = df_results.set_index("day")
    summary_output = wofsim.get_summary_output()
