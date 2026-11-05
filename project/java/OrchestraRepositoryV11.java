package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0, 1.1-rc3 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  A machine-readable set of rules of engagement: the datatypes, code sets, fields, components, groups and messages it defines, and the actors and workflows that use them.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class OrchestraRepositoryV11  {

  private OrchestraMetadata fixrMetadata;
  private OrchestraCategoriesV11 fixrCategories;
  private OrchestraSectionsV11 fixrSections;
  private OrchestraEncodingStandardsV11 fixrEncodingStandards;
  private OrchestraDatatypesV11 fixrDatatypes;
  private OrchestraCodeSetsV11 fixrCodeSets;
  private OrchestraFieldsV11 fixrFields;
  private OrchestraActorsV11 fixrActors;
  private OrchestraComponentsV11 fixrComponents;
  private OrchestraGroupsV11 fixrGroups;
  private OrchestraMessagesV11 fixrMessages;
  private OrchestraConceptsV11 fixrConcepts;
  private OrchestraScenariosV11 fixrScenarios;
  private OrchestraAnnotationV11 fixrAnnotation;
  private String fixrName;
  private String fixrVersion;
  private String fixrGuid;
  private URI fixrSpecUrl;
  private URI fixrNamespace;
  private String fixrExpressionLanguage;


}