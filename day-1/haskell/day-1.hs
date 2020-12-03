import qualified Data.Set as Set

sumsTo2020 :: Integral a => [a] -> Set.Set a -> (a, a)
sumsTo2020 (x : xs) set
  | (2020 - x) `Set.member` set = (2020 - x, x)
  | otherwise = sumsTo2020 xs set

productThatSumsTo2020 :: Integral a => [a] -> Maybe a
productThatSumsTo2020 [] = Nothing
productThatSumsTo2020 list =
  let (a, b) = sumsTo2020 list (Set.fromList list)
  in Just $ a * b

main :: IO ()
main = do
  f <- readFile "../input.txt"
  let entries = map (\x -> read x :: Int) (lines f)
  case productThatSumsTo2020 entries of
    Nothing -> putStrLn "Not found"
    Just n -> putStrLn . unwords $ ["Found", show n]
