#!user/bin/env ruby

#Keep three arrays, which represents the piles of discs. Pick a representation of the discs to store in the arrays; maybe just a number representing their size.
#In a loop, prompt the user (using gets) and ask what pile to select a disc from, and where to put it.
#After each move, check to see if they have succeeded in moving all the discs, to the final pile. If so, they win

winning_pile = [1, 2, 3, 4]
p1 = [1, 2, 3, 4] # pile 1, acending order of disk size
p2 = []
p3 = []

def condition(input, pile1, pile2, pile3)
  if input == pile1[0]
    pile1.delete_at(0)
  elsif input == pile2[0]
    pile2.delete_at(0)
  elsif input == pile3[0]
    pile3.delete_at(0)
  end
end

puts ''
puts "TOWERS OF HANOI"
puts ''
puts 'Let\'s PLay'

loop do
  puts ''
  print "p1 = #{p1}"
  puts ''
  print "p2 = #{p2}"
  puts ''
  print "p3 = #{p3}"
  puts ''
  puts "select a disk"
  disk = gets.chomp.to_i
  unless (disk == p1[0] || disk == p2[0] || disk == p3[0]) && (disk != nil)
    loop do
      puts "please select the top existing disk from any pile"
      disk = gets.chomp.to_i
      if (disk == p1[0] || disk == p2[0] || disk == p3[0]) && (disk != nil)
      break
      end
    end
  end
  
  def condition(input, pile1, pile2, pile3)
    if input == pile1[0]
      pile1.delete_at(0)
    elsif input == pile2[0]
      pile2.delete_at(0)
    elsif input == pile3[0]
      pile3.delete_at(0)
    end
  end
  
  puts "Which pile would you like to stack this disk on?"
  pile = gets.chomp
  if pile == 'p1' && (p1[0] == nil || disk < p1[0] )
    condition(disk, p1, p2, p3)
    p1.unshift(disk)
  elsif pile == 'p2' && (p2[0] == nil || disk < p2[0])
    condition(disk, p1, p2, p3)
    p2.unshift(disk)
  elsif pile == 'p3' && (p3[0] == nil || disk < p3[0])
    condition(disk, p1, p2, p3)
    p3.unshift(disk)
  else
    puts "You can't do that!"
  end
  
  if p3 == winning_pile  # easy version: p2 == winning_pile || p3 == winning_pile
    puts "WE HAVE A WINNER!!!"
    break
  end
end


#https://repl.it/@LukeDreyer/arrayPractice
