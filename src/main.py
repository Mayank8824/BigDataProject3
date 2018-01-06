import classifiers
import features
import metrics

def main():
	# data frame with our dataset
	df = get_BAS_dataset()

	# preprocessing of the data to capture the features we want
	df_features_class_A = get_class_A_features(df)
	df_features_class_C = get_class_C_features(df)

	# classifiers (training + prediction)
	class_A_classifiers = classify(df_features_class_A)
	class_C_classifiers = classify(df_features_class_C)

	# Metrics on the result predictions from the classifiers
	results_class_A_classifiers = metrics(class_A_classifiers)
	results_class_C_classifiers = metrics(class_C_classifiers)

	# publish and save results
	publish(results_class_A_classifiers)
	publish(results_class_C_classifiers)


if(__name__ == "__main__"):
	main()