#윷놀이 계산기
import random as rt
while True:
          game = int(input("1.play / 2. end       "))
          if game == 1:
                    yot1 = rt.randint(0,1)
                    yot2 = rt.randint(0,1)
                    yot3 = rt.randint(0,1)
                    yot4 = rt.randint(0,1)
                    print(yot1, yot2, yot3,yot4)
                    add = yot1+yot2+yot3+yot4
                    goal = 20
                    side = 5
                    passcount = 0
                    if add == 1:
                              if yot1 == 1:
                                        print("백도")
                                        goal += 1
                                        side += 1
                                        if side == 0:
                                                  side = 3
                                                  if passcount == 0:
                                                            goal = 11
                                                  elif passcount == 3:
                                                            goal = 2
                                                  else:
                                                            goal = 6
                                        elif side < 0:
                                                  side = 5 + side
                                                  passcount += 1
                                        print("다음 지름길까지", side, "만큼 남았습니다")
                                        print("도착까지", goal, "만큼 남았습니다")
                                        
                              else:
                                        print("도")
                                        goal += -1
                                        side += -1
                                        if side == 0:
                                                  side = 3
                                                  if passcount == 0:
                                                            goal = 11
                                                  elif passcount == 3:
                                                            goal = 2
                                                  else:
                                                            goal = 6
                                        elif side < 0:
                                                  side = 5 + side
                                                  passcount += 1
                                        print("다음 지름길까지", side, "만큼 남았습니다")
                                        print("도착까지", goal, "만큼 남았습니다")
                                        
                    elif add == 2:
                              print("개")
                              goal += -2
                              side += -2
                              if side == 0:
                                        side = 3
                                        if passcount == 0:
                                                  goal = 11
                                        elif passcount == 3:
                                                  goal = 2
                                        else:
                                                  goal = 6
                              elif side < 0:
                                        side = 5 + side
                                        passcount += 1
                              print("다음 지름길까지", side, "만큼 남았습니다")
                              print("도착까지", goal, "만큼 남았습니다")
                              
                    elif add == 3:
                              print("걸")
                              goal += -3
                              side += -3
                              if side == 0:
                                        side = 3
                                        if passcount == 0:
                                                  goal = 11
                                        elif passcount == 3:
                                                  goal = 2
                                        else:
                                                  goal = 6
                              elif side < 0:
                                        side = 5 + side
                                        passcount += 1
                              print("다음 지름길까지", side, "만큼 남았습니다")
                              print("도착까지", goal, "만큼 남았습니다")

                    elif add == 4:
                              print("윷")
                              goal += -4
                              side += -4
                              if side == 0:
                                        side = 3
                                        if passcount == 0:
                                                  goal = 11
                                        elif passcount == 3:
                                                  goal = 2
                                        else:
                                                  goal = 6
                              elif side < 0:
                                        side = 5 + side
                                        passcount += 1
                              print("다음 지름길까지", side, "만큼 남았습니다")
                              print("도착까지", goal, "만큼 남았습니다")
                    elif add == 0:
                              print("모")
                              goal += -5
                              side += -5
                              if side == 0:
                                        side = 3
                                        if passcount == 0:
                                                  goal = 11
                                        elif passcount == 3:
                                                  goal = 2
                                        else:
                                                  goal = 6
                              elif side < 0:
                                        side = 5 + side
                                        passcount += 1
                              print("다음 지름길까지", side, "만큼 남았습니다")
                              print("도착까지", goal, "만큼 남았습니다")
          if game == 2 or goal == 0:
                    print("Game Over")
                    break
