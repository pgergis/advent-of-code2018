import qualified Data.Counter as C
import qualified Data.Map as M

type HasTwos = Bool
type HasThrees = Bool

hasTwosOrThrees :: String -> (HasTwos, HasThrees)
hasTwosOrThrees line = (keysWithTwos /= [], keysWithThrees /= [])
  where charFreqCounter = C.count line
        keysWithTwos = M.keys $ M.filter (\n -> n == 2) charFreqCounter
        keysWithThrees = M.keys $ M.filter (\n -> n == 3) charFreqCounter

countTrues :: [Bool] -> Int
countTrues bools = foldl (flip ((+) . fromEnum)) 0 bools

linesWithTwosOrThrees :: [(HasTwos, HasThrees)] -> (Int, Int)
linesWithTwosOrThrees counts =
  let twosThrees = unzip counts
      hasTwosList = fst twosThrees
      hasThreesList = snd twosThrees
  in
    (countTrues hasTwosList, countTrues hasThreesList)

checksum :: [String] -> Int
checksum lines = twos * threes
  where (twos, threes) = linesWithTwosOrThrees $ map hasTwosOrThrees lines

main :: IO ()
main = do
  f <- readFile("../inputs/02-input")
  putStrLn $ show $ checksum $ lines f
