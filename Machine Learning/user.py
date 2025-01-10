def Fun():
    
    # Load data
    X = [1,2,3,4,5]
    Y = [3,4,2,4,5]
    
    n =len(X)

    Sum_x = 0
    Sum_y = 0
    
    for i in range (n):
        Sum_x +=X[i]
        Sum_y +=Y[i]
        
        
    mean_x = Sum_x / n   
    mean_y = Sum_y / n   

    numerator = 0          
    denomenator = 0
    
    # Equation of line is y = mx + c

    for i in range(n):
        numerator += (X[i] -mean_x)*(Y[i] - mean_y)
        denomenator += (X[i] - mean_x)**2   #   ** is power of x

    m = numerator / denomenator

    c = mean_y - (m * mean_x)

    print("Slope of Regression line is",m)
    print("Y intercept of Regression line is",c)

    # Findout goodness of fit...ie R Square
    ss_t = 0
    ss_r = 0

    for i in range(n):
        y_pred = c + m *X[i]
        ss_t += (Y[i] - mean_y) ** 2
        ss_r += (Y[i] - y_pred) ** 2

    r2 = 1 - (ss_r/ss_t)     #R Square 

    print(r2)

def main():
    
    print("This Is Program For Getting Linear Regression by USER Defined")

    Fun()

if __name__ == "__main__":
    main()
