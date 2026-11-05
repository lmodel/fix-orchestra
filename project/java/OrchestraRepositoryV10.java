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
public class OrchestraRepositoryV10  {

  private OrchestraMetadata fixrMetadata;
  private OrchestraCategoriesV10 fixrCategories;
  private OrchestraSectionsV10 fixrSections;
  private OrchestraDatatypesV10 fixrDatatypes;
  private OrchestraCodeSetsV10 fixrCodeSets;
  private OrchestraFieldsV10 fixrFields;
  private OrchestraActorsV10 fixrActors;
  private OrchestraComponentsV10 fixrComponents;
  private OrchestraGroupsV10 fixrGroups;
  private OrchestraMessagesV10 fixrMessages;
  private OrchestraConceptsV10 fixrConcepts;
  private OrchestraAnnotationV10 fixrAnnotation;
  private String fixrName;
  private String fixrVersion;
  private String fixrGuid;
  private URI fixrSpecUrl;
  private URI fixrNamespace;
  private String fixrApplVerId;
  private String fixrExpressionLanguage;
  private Integer fixrLatestEp;


}