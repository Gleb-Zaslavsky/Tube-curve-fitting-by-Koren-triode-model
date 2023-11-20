# Tube-curve-fitting-by-Koren-triode-model
The Python code for vacuum tube models: takes a datasheet image of the graphical dependence of anode current on anode-cathode voltage at different grid voltages and returns the parameters of the Koren model for the SPICE simulations
  ENG
1) in the File menu select a graphical file containing a graph from the datasheet of anode current vs. anode-cathode voltage at different grid currents.
2) If there are empty edges on the graph, crop them using any graphic editor or the "crop image" option in the "data processing" menu
3) Enter the current and voltage range in the four fields on the GUI (maximum and minimum current and voltage).
4) enter grid voltage in the corresponding field and click on "input grid V" button.
5) click with the mouse on the points of the anode current-anode voltage curve corresponding to the entered grid voltage, usually 7-10 points are enough.
6) when you are done with one grid voltage, enter the next one and click "input grid V" and so on.
7) enter the triode name in the "tube name" field
8) in the "data processing" menu select "fit with Koren model".
9) the fitting results will appear in the terminal 
10) click on "update image" button, the datasheet picture will appear with the fitting result overlaid on top of it
11) Enjoy the result!


RUS
1) в меню Файл выберите графический файл содержащий график из даташита зависимости  тока анода от напряжения анод-катод при разных токах сетки.
2) Если на рисунке имеются пустые края обрежьте их используя любой графический редактор или опцию "crop image" в меню "data processing"
3) введите область значений тока и напряжения в четыре поля на GUI (максимальные и минимальные ток и напряжение)
4) введите напряжение на сетке в соответствующее поле и нажмите на кнопку "input grid V"
5) мышкой нажимайте на точки кривой ток анода-напряжение на аноде соответствующей введенному напряжению на сетке, обычно достаточно 7-10 точек
6) когда закончите с одним напряжением на сетке введите следующее и нажмите "input grid V" и так далее
7) введите в поле "tube name" название триода
8) меню  "data processing" выберите "fit with Koren model"
9) в терминале появятся результаты фиттинга 
10) нажмите на кнопку "update image" появится рисунок из даташита с наложенным сверху результатом фиттинга
11) Наслаждайтесь результатом!
    
