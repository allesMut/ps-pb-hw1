import time
import os

slide1 = '''                                       
                                    $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
             $$$$$$$  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$        $          $$$$$$$  $$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$      $$$$$$$       $$$$$$$  $$$$$$$$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$      $$$$$$$     $$$        $$$$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$        $                  $$$$$$$$$$$$$$$$$$ 
  $$$$$$$$$$$$$$$$$$$$$$$$$$                   $      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$                      $$$$$$$$$$$$$$$$$$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$            $$$$$ $$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
  $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
   $$$$$$$$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
    $$$$$$$$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
     $$$$$$$$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
              $$$          $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

slide2 = '''                                       
                                    $$$$$$$$
                                $$$$$$$$$$$$$$$$$$
                             $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                          $$$$$$$$$$$$$$$$ $      $$$$$$$$$$$$$$$$$$$
                        $$$$$$$$$$$               $$ $$$$$$$$$$$$$$$$$$
                       $$$$$$$$ $$$                    $$$$$$$$$$$$$$$$$
                   $  $$$$$$$                   $$$$$  $$$$$$$$$$$$$$$$$$
               $$$$$$$$$$$$$                   $$$$$$$  $$$$$$$$$$$$$$$$$
             $$$$$$$$$$$$$$    $$$$$$$$        $$$$$$$  $$$$$$$$$$$$$$$$$$
           $$$$$$$$$$$$$$$$     $$$$$$$$        $$$$$   $$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$                             $$$$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$       $$                  $$$$$$$$$$$$$$$$$$ 
        $$$$$$$$$$$$$$$$$$$$         $$$              $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$          $$$$$$      $$$$$$$$$$$$$$$$$$
       $$$$$$$$$$$$$$$$$$$$$$$$$                  $$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
        $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$ $$$$$$$$$$$$$$$$
         $$$$$$$$$$$$$$$$$$$$ $$ $$ $  $$$$$$$$$$$$$$$$$$$$$
          $$$$$$$$$$$$$$$$$$$   $ $$$$$$$    $$ $$$$$$$$$$$$
           $$$$$$$$$$$$$$$   $$$$$$$$      $ $$$$$$$$$$$$$$
              $$$$$$$$$     $$$$$$$$$$    $  $$$$$ $$$$$$$
                    $$$    $$$$ $$$$  $$ $ $$$$$ $$$$$
                            $$$$ $$$  $   $ $$ $$$$ $$
                            $$$$$$$     $ $ $$$$$$$$$$$
                             $$$$$$ $$$  $ $$$$$$$$$$$$
                               $$$$$$$$$$$$$$$$$$$$$$$
                                $$$$$$$$$$$$$$$$$$$$$$
                              $$$$$$$$$$$$$$$$$$$$$ $$$$
                            $$$$$$$$$$$$$$$$ $$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
                           $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'''

qtyCadr = 7 #требуемое количество кадров
i = 0 #номер текущего кадра

while i <= qtyCadr:
    os.system('cls') #очистка экрана
    if i % 2 == 0: #выбор кадра
        viewCadr = slide1
    else:
        viewCadr = slide2
    print(viewCadr, end='\r') #вывод на экран кадра и перевод каретки в начальную позицию
    i += 1
    time.sleep(1) #Задержка между кадрами
else: #исключительно факультативно
    os.system('cls') #очистка экрана
    print('The End') #вывод на экран текста и перевод каретки в начальную позицию
