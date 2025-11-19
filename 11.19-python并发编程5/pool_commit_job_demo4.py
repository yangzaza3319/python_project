from multiprocessing import Pool

def square(x):
    return x*x

def collect_result(result,result_list):
    result_list.append(result)

if __name__=="__main__":
    with Pool(4) as pool:
        results = []
        for i in range(10):
            pool.apply_async(square,(i,),callback=lambda r:collect_result(r,results))
            pool.close()
            pool.join()
            print("最后结果:",sorted(results))