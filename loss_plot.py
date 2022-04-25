epochs = []
for i in range(10):
    epochs.append(i+1)
train_loss_total = []
train_loss_giou = []
train_loss_l1 = []
val_loss_total = []
val_loss_giou = []
val_loss_l1 = []

for i in range(10):
    train_loss_l1.append(0)
    train_loss_total.append(0)
    train_loss_giou.append(0)
    val_loss_l1.append(0)
    val_loss_giou.append(0)
    val_loss_total.append(0)

def get_loss_total(line):
    temp = line.split(', ')
    temp_1 = temp[2].split(':')
    temp_1 = temp_1[1].split(' ')
    temp = temp_1[1]
    temp=float(temp)
    return temp

def get_loss_giou(line):
    temp = line.split(', ')
    temp_1 = temp[3].split(':')
    temp_1 = temp_1[1].split(' ')
    temp = temp_1[1]
    temp = float(temp)
    return temp

def get_loss_l1(line):
    temp = line.split(', ')
    temp_1 = temp[4].split(':')
    temp_1 = temp_1[1].split(' ')
    temp = temp_1[1]
    temp = float(temp)
    return temp

filename = 'train_val_results.txt'
with open(filename, 'r') as f:
    lines = f.readlines()
    j = 1
    i = 1
    for line in lines:
        for i in range(10):

            train_test = 'train: '+ str(i+1)
            val_test = 'val: '+str(i+1)
            if train_test in line:
                train_loss_total[i] = train_loss_total[i] + get_loss_total(line)
                train_loss_giou[i] =  train_loss_giou[i] + get_loss_giou(line)
                train_loss_l1[i] = train_loss_l1[i] + get_loss_l1(line)
            if val_test in line:
                val_loss_total[i] =val_loss_total[i] + get_loss_total(line)
                val_loss_giou[i] = val_loss_giou[i] + get_loss_giou(line)
                val_loss_l1[i] = val_loss_l1[i] + get_loss_l1(line)


for i in range(10):
    train_loss_total[i] = train_loss_total[i]/150
    train_loss_giou[i] =train_loss_giou[i]/150
    train_loss_l1[i] = train_loss_l1[i]/150
    val_loss_total[i] = val_loss_total[i]/25
    val_loss_giou[i] = val_loss_giou[i]/25
    val_loss_l1[i] = val_loss_l1[i]/25

print(train_loss_total)
print(train_loss_giou)
print(train_loss_l1)
print(val_loss_total)
print(val_loss_giou)
print(val_loss_l1)

import matplotlib.pyplot as plt

plt.figure()
plt.plot(epochs, train_loss_total, 'bo', label='train total loss')
plt.plot(epochs, val_loss_total, 'b', label='val total loss')
plt.title('Training and validation total loss')
plt.legend()
plt.show()

plt.figure()
plt.plot(epochs, train_loss_giou, 'bo', label='train giou loss')
plt.plot(epochs, val_loss_giou, 'b', label='val giou loss')
plt.title('Training and validation giou loss')
plt.legend()
plt.show()

plt.figure()
plt.plot(epochs, train_loss_l1, 'bo', label='train l1 loss')
plt.plot(epochs, val_loss_l1, 'b', label='val l1 loss')
plt.title('Training and validation l1 loss')
plt.legend()
plt.show()


        