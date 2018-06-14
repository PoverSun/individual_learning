def make_shirt(shirt_size='大号',shirt_fontstyle='I love Python!'):
    print('制作一个印有%s的%sT恤'%(shirt_fontstyle,shirt_size))
print('\n一件印有默认字样的大号T恤：')
make_shirt(shirt_size='大号',shirt_fontstyle='I love Python!')

print('\n一件印有默认字样的中号T恤：')
make_shirt(shirt_size='中号',shirt_fontstyle='I love Python!')

print('\n一件印有其他字样的小号T恤：')
make_shirt(shirt_size='小号',shirt_fontstyle='Hello  Python!')
