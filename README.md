Hallgató: Balogh Dániel (BD) – QN3RRK

Beadandó: Edzésnapló alkalmazás



Rövid leírás:

A program egy egyszerű edzésnapló alkalmazás, amelyben a felhasználó rögzítheti az elvégzett edzéseket: dátum, gyakorlat neve, ismétlésszám és használt súly.

Az adatok egy CSV fájlba kerülnek mentésre, így a program újraindítás után automatikusan visszatölti a korábbi bejegyzéseket.

A felület Tkinterrel készült, a súlyfejlődés pedig egy beépített Canvas alapú grafikonon jelenik meg.



Fájlok és modulok:

main.py  
– A grafikus felület indítása.

bd_app.py  
– A teljes Tkinter alapú grafikus felület.  
  Fontosabb metódusok:  
  add_entry  
  delete_entry  
  save  
  show_max_weight  
  show_graph  
  exit_app

bd_workout_module.py  
– Külön modul az edzésadatok kezelésére.  
  BDEdzes osztály: date, exercise, reps, weight  
  to_list  
  bd_max_weight

bd_data_handler.py  
– Fájlkezelés és dátumkezelés.  
  save_to_csv  
  load_from_csv  
  format_date

bd_visualize.py  
– A grafikon megjelenítése Tkinter Canvas segítségével.  
  show_weight_progress



Osztályok:

BDEdzes (bd_workout_module.py)  
Attribútumok: date, exercise, reps, weight  
Metódus: to_list – CSV exporthoz szükséges lista előállítása
