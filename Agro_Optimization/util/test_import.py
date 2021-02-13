if __name__ == "__main__":
    import time
    start = time.time()

    from main_crop_model import Irrigation
    WOFOST = Irrigation()
    status, info = WOFOST.compute('./input_data/', 'winter_wheat.json', '/Users/mikhailgasanov/Documents/machine_learning/NASA_CSV','./images/varishi_report.png', 2, './images/varishi.png')


    print(f'___DONE:{status}, time:{time.time()-start}, Problems? {info}')