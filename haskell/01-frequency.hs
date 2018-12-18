import qualified Data.Map as M

type Op = Char
type FreqMap = M.Map Int Int

parseInput :: String -> [(Op, Int)]
parseInput fileString = map parseLine $ lines fileString

parseLine :: String -> (Op, Int)
parseLine l = (head l, read $ tail l)

adjustFreq :: Int -> (Op, Int) -> Int
adjustFreq m ('+', n) = m + n
adjustFreq m ('-', n) = m - n
-- adjustFreq _ (_, _) =

frequencyCalculator :: Int -> [(Op,Int)] -> Int
frequencyCalculator start ops = foldr (flip adjustFreq) start ops

loopCalculator :: FreqMap -> Int -> [(Op,Int)] -> [(Op,Int)] -> Int -> Int
-- loopCalculator _ _ _ [] =
loopCalculator seen start remainingOps origOps iterations =
  if M.member start seen
  then start
  else
    if remainingOps == []
    then loopCalculator seen start origOps origOps (iterations+1)
    else loopCalculator (M.insert start 1 seen) (adjustFreq start $ head remainingOps) (tail remainingOps) origOps iterations

main :: IO ()
main = do
  f <- readFile "../inputs/01-input"
  putStr "First pass result: "
  putStrLn $ show $ frequencyCalculator 0 $ parseInput f
  putStr "Result first to appear twice: "
  putStrLn $ show $ loopCalculator M.empty 0 (parseInput f) (parseInput f) 0
