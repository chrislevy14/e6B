, end = '\r')
                time.sleep(1)
            if sec == 0 and min == 0:
                timerDone = True
                break
        except KeyboardInterrupt: ## Need a better way to kill the program.
            break