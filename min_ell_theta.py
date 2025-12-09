def learn_theta(data, colors):
   
    max_blue = None
    min_red = None
    
    for i in range(len(data)):
        if colors[i] == 'blue':
            if max_blue is None or data[i] > max_blue:
                max_blue = data[i]
        else:  
            if min_red is None or data[i] < min_red:
                min_red = data[i]
    
    return (max_blue + min_red) / 2


def compute_ell(data, colors, theta):
    loss = 0.0
    
    for i in range(len(data)):
        if colors[i] == 'red' and data[i] <= theta:
            loss += 1
        elif colors[i] == 'blue' and data[i] > theta:
            loss += 1
    
    return loss


def minimize_ell(data, colors):
    n = len(data)
    
    sorted_data = sorted(data)
    
    best_theta = None
    best_loss = float('inf')
    for i in range(n - 1):
        theta = (sorted_data[i] + sorted_data[i + 1]) / 2
        loss = compute_ell(data, colors, theta)
        
        if loss < best_loss:
            best_loss = loss
            best_theta = theta
    
    return best_theta


def minimize_ell_sorted(data, colors):
    n = len(data)
    total_blue = sum(1 for c in colors if c == 'blue')
    
    red_leq_theta = 0
    blue_gt_theta = total_blue
    
    best_loss = red_leq_theta + blue_gt_theta
    best_theta = data[0] - 1  
    
    for alpha in range(n):
        if colors[alpha] == 'red':
            red_leq_theta += 1
        else: 
            blue_gt_theta -= 
        current_loss = red_leq_theta + blue_gt_theta
        
        if current_loss < best_loss:
            best_loss = current_loss
            if alpha < n - 1:
                best_theta = (data[alpha] + data[alpha + 1]) / 2
            else:
                best_theta = data[alpha] + 1  
    
    return best_theta
